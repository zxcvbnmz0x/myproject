//document.write("<script src='/static/js/histogram.js'></script>");
//document.write("<link rel='stylesheet' href='/static/css/histogram.css'></script>");
document.write("<script src='/static/js/utils.js'></script>");
document.write("<script src='/static/js/tools.js'></script>");

$(function(){
    var showitem = 'location_card';
	//基础单位
	var basicUnit = '';
	var startpostion = 0;
	var page = 1;//当前的页面
	var stufflist = new Array();
	//根据屏幕方式转屏
    transalewindow();
	$('#topage').click(function(e){
	    let thispage = $(":text").val();
	    let r = /^\+?[1-9][0-9]*$/;　　
	    //正整数
	    if(r.test(thispage) )
	    {
	        if(page != thispage)
	        {
	            page = thispage;
	            $('#location_card').find('*').hide();
                showstuff(stufflist.slice((thispage-1)*5,thispage*5));
                flashnav();
	        }

	    }
	    else
	    {
	        alert("输入异常，页码范围：1到"+Math.ceil(stufflist.length/5));
	    }

	});

	//取得地址栏中的参数
	let pararmeters = getUrlparameter();

    if(pararmeters)
    {
        createHeaderhander( "searchstuff",pararmeters);
	}
    else
    {
        $('#location_card').find('*').remove();
        $("#nav").find('*').remove();
        $('#location_card').append("<h1>参数异常或者没有找到对应的物料信息</h1>");
    }

	/*
	 * 获取数据库中仓库的类型
	 * */
	 function createHeaderhander(init_data_url,parmeters)
	 {
		var batchno,stuffid;
		//promise异步请求获得货位卡对应的物料信息
		p = runAsync(init_data_url,parmeters);
		p.then(function(stuff)
		{
		    if(stuff.length == 0)
		    {
		        $('#location_card').find('*').remove();
		        $("#nav").find('*').remove();
                $('#location_card').append("<h1>该货位卡没有相应的物料信息</h1>");
		    }
		    else
		    {
		        let count = 0;
		        stufflist = stuff;
		        if(Math.ceil(stuff.length/5)>10)
		        {
		            count = 3;
                    for (let i = 1;i <= 10;i++)
		            {
		                if(i<6)
		                {
		                    $("#paging").append('<li class = "pagelag pagination-sm"><span aria-hidden="true">'+i+'</span></li>');
		                }
		                if(i==6)
		                {
		                    $("#paging").append('<li class = "pagination-sm"><span aria-hidden="true">......</span></li>');
		                }
		                if(i>6)
		                {
		                    $("#paging").append('<li class = "pagelag pagination-sm"><span aria-hidden="true">'+(Math.ceil(stuff.length/5)-count)+'</span></li>');
		                    count--;
		                }
		            }
		        }
		        else
		        {
		            for (let i = 0;i <= stuff.length;i+=5)
		            {
		                count++;
		                $("#paging").append('<li class = "pagemin"><span aria-hidden="true">'+count+'</span></li>');
		            }
		        }

		        $("#paging").append('<li class = "nextPage"><span aria-hidden="true">&raquo;</span></li>');
                showstuff(stuff.slice(0,5));
                clickfunction(page);

			}
		});
		p.catch(function()
		{
		   console.error('Something was wrong');
		});
	 }


/*
 * 参数row_data：行中每个td的内容
 * 参数num，行号
 * basicUnit：基础单位
 */
function create_row(row_data,num,basicUnit,useamount = 0)
{
    var row_obj = $("<tr></tr>");
    for(var k in row_data)
	{
	    var col_td = $("<td></td>");
	    if(k == 'useamount')
	    {
	        nextAmount = nextAmount + parseFloat(row_data[k]);
            supAmount = nextAmount.toFixed(3) + basicUnit;
            col_td.html(supAmount);
            row_obj.append(col_td);
		}
		else if(k == 'inamount' || k == 'outamount')
		{
			col_td.html(row_data[k] + basicUnit);
			row_obj.append(col_td);
		}
		else
		{
			col_td.html(row_data[k]);
			row_obj.append(col_td);
		}
	}
    return row_obj;
}

/*
 * 异步获得检验报告编号
 * 然后通过createFormHeader()生成表头信息
 * 通过iodetail()生成详细出入库记录
 */
function labdetail(stuffitem,num)
{
    //获得报告单号，promise请求
	init_data_url= "/labrecord/getlabrecord";
    detail = getlabrecord(init_data_url,stuffitem.lrid);
    detail.then(function (labRecordRes)
    {
        //判断是否找到报告
        if(labRecordRes.length > 0 )
        {
            stuffitem.paperno = labRecordRes[0].fields.paperno;
        }
        else
        {
            stuffitem.paperno = "/";
        }
        stuffid = stuffitem.stuffid;
        batchno = stuffitem.batchno;
        createFormHeader(stuffitem,num);
        iodetail(stuffitem,num);
    });

}
/*
 * 初始化表格内容
 * 返回表格序号num
 */
    function creatediv()
    {
        itemid = $('#location_card div:last-child').attr("id");
	    if( typeof(itemid) == "undefined")
	    {
	        itemid = "item_0";
	        num = parseInt(itemid.substr(5));
	    }
	    else
	    {
	        num = parseInt(itemid.substr(5))+1;
	    }

	    var div = '<div id = "item_'+num+'"class="col-md-12 stuffiolist" role="main" id="content">';
	    var table1 = '<h1 id = title_'+num+'></h1><table><tr><td id="stuffname_'+num+'">物料名称：</td><td id="packagespec_'+num+'">包装规格：</td> <td id="batchno_'+num+'">批号：</td><td id="source_'+num+'">来源：</td></tr><tr><td id="firstamount_'+num+'">入库数量：</td><td id="nowamount_'+num+'">当前数量：</td><td id="paperno_'+num+'">报告单号：</td><td id="checkdata_'+num+'">复检期：</td></tr></table>';
	    var table2 = '<table id="stufftable_'+num+'" class="table table-bordered table-striped table-hover" ><thead><tr><td>日期</td><td>类型</td><td>收入量</td><td>发出量</td><td>结存量</td><td>发料人</td></tr></thead></table></div>';
	    $('#location_card').append(div+table1+table2);
        return num;
    }

/*
 * 添加查询的总信息
 */
	function createFormHeader(content,num)
	{
		var stuffname = $("#stuffname_"+num);
		var packagespec = $("#packagespec_"+num);
		var batchno = $("#batchno_"+num);
		var source = $("#source_"+num);
		var paperno = $("#paperno_"+num);
		var checkdata = $("#checkdata_"+num);
        var firstAmount = $("#firstamount_"+num);
		var nowAmount = $("#nowamount_"+num);
        var title = $("#title_"+num);

		var stuffnameHtml = content.stuffid+ ' ' +content.stuffname;
		var packagespecHtml = content.package;
		var batchnoHtml = content.batchno;
		var sourceHtml = content.producer;
		var papernoHtml = content.paperno;
		var checkdataHtml = content.checkdate;
        var inAmountHtml = content.piamount + content.basicunit;
		var amountHtml = content.amount + content.basicunit;
        var titleHtml = content.stuffname+content.batchno+"批次货位卡";

		stuffname.append(stuffnameHtml);
		packagespec.append(packagespecHtml);
		batchno.append(batchnoHtml);
		source.append(sourceHtml);
		paperno.append(papernoHtml);
		checkdata.append(checkdataHtml);
        firstAmount.append(inAmountHtml);
		nowAmount.append(amountHtml);
		title.append(titleHtml);
	}

/*
 * 首先异步请求获得详细的出入库记录
 * 然后把返回的记录通过循环的方法取得每一行的值
 * 使用create_row()生产每一行的html元素
 */
function iodetail(stuffitem,num)
{
    init_data_url= "showstuffiodetail";
    detail = getdetail(init_data_url+'?stuffid='+stuffitem.stuffid+'&batchno='+stuffitem.batchno)
    detail.then(function(row_items)
    {
        var g_table = $("#stufftable_"+num);
        nextAmount = 0;
        for( var k in row_items )
        {
            var data_dom = create_row(row_items[k],num,stuffitem.basicunit);
            //lineNum[i]=data_dom;
            g_table.append(data_dom);
        }
    });
}

function clickfunction()
{

                $('.pagemin').click(function(e)
                {
                    let newPage = e.target.textContent;

                    if (newPage != page)
                    {
                        $('#location_card').find('*').hide();
                        showstuff(stufflist.slice((newPage-1)*5,newPage*5));
                        page = newPage;
                        flashnav();
                    }
                });
                $('.pagelag').click(function(e)
                {
                    let newPage = e.target.textContent;
                    if (newPage != page)
                    {
                        $('#location_card').find('*').hide();
                        showstuff(stufflist.slice((newPage-1)*5,newPage*5));
                        page = newPage;
                        flashnav();
                    }
                });
                $('.previousPage').click(function(e)
                {
                    if (page != 1)
                    {
                        page--;
                        $('#location_card').find('*').hide();
                        showstuff(stufflist.slice((page-1)*5,page*5));
                        flashnav();
                    }
                });
                $('.nextPage').click(function(e)
                {
                    if (page != Math.ceil(stufflist.length/5))
                    {
                        page++;
                        $('#location_card').find('*').hide();
                        showstuff(stufflist.slice((page-1)*5,page*5));
                        flashnav();
                    }
                });
}

function showstuff(stuff)
{
    for(key in  stuff)
                {
                    this.basicUnit = stuff[key].basicunit;
			        var batchno = stuff[key].batchno;
			        var stuffid = stuff[key].stuffid;
			        var stuffitem = stuff[key];
			        lrid = stuffitem.lrid;
			        //建立本次循环物料对应的表格，并返回id的后缀编号
			        num = parseInt(creatediv());
                    labdetail(stuffitem,num)

//			        createFormHeader(stufitem,num);
			    }
}
/*
 * 刷新分页栏
 */
function flashnav()
{
    //判断页数是否大于10，少于等于就无需刷新
    if(Math.ceil(stufflist.length/5)>10)
    {
        //删除旧的分页
        $("#paging").find('*').hide();
        //重新增加《
        $("#paging").append('<li class = "previousPage"><span aria-hidden="true">&laquo;</span></li>');
        //设置当前页号码为起始页码
        let thispage = page;
        let count = 3;
        //判断当前页面到最后的页面是否大于10
        if(Math.ceil(stufflist.length/5)-thispage>10)
		{
		    for (let i = 1;i <= 10;i++)
            {
		        if(i<6)
		        {
		            $("#paging").append('<li class = "pagelag"><span aria-hidden="true">'+thispage+'</span></li>');
		        }
		        if(i==6)
		        {
		            $("#paging").append('<li><span aria-hidden="true">......</span></li>');
		        }
		        if(i>6)
		        {
		            $("#paging").append('<li class = "pagelag"><span aria-hidden="true">'+(Math.ceil(stufflist.length/5)-count)+'</span></li>');
		            count--;
		        }
		        thispage++;
		    }
		}
		else
		{
		    for (let i = Math.ceil(stufflist.length/5)-10;i <= Math.ceil(stufflist.length/5);i++)
		    {
		        $("#paging").append('<li class = "pagemin"><span aria-hidden="true">'+i+'</span></li>');
		    }
		}

    $("#paging").append('<li class = "nextPage"><span aria-hidden="true">&raquo;</span></li>');
    clickfunction();
    }
}



});


