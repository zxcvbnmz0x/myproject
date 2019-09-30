document.write("<script src='/static/js/utils.js'></script>");
document.write("<script src='/static/js/tools.js'></script>");
var showitem = 'location_card';
//基础单位
var basicUnit = '';
var startpostion = 0;
var page = 1;//当前的页面
var stufflist = new Array();
$(function()
{
    //根据屏幕方式转屏
    transalewindow();
	let parmeters = getUrlparameter();
    createHeaderhander( "searchproduct",parmeters);

	/*
	 * 获取数据库中仓库的类型
	 * */
	 function createHeaderhander(init_data_url,parmeters)
	 {
		//promise异步请求获得货位卡对应的物料信息
		p = runAsync(init_data_url,parmeters);
		p.then(function(stuff)
		{
		    if(stuff.length == 0)
		    {
		        $('#location_card').find('*').remove();
		        $("#nav").find('*').remove();
                $('#location_card').append("<h1>没有相应的物料信息</h1>");
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
                showstufflist(stuff.slice(0,5));
                clickfunction(page);

			}
		});
		p.catch(function()
		{
		   console.error('Something was wrong');
		});
	 }





});

$(document).ready(function(){

     $('#clickselector').click(function()
     {
	    $('#selector').slideToggle(500);
	});
	$('#topage').click(function(e){
	    let thispage = $(":text").val();
	    let r = /^\+?[1-9][0-9]*$/;　　
	    //正整数
	    if(r.test(thispage) )
	    {
	        if(page != thispage)
	        {
	            page = thispage;
	            $('tbody').find('*').hide();
                showstufflist(stufflist.slice((thispage-1)*5,thispage*5));
                flashnav();
	        }

	    }
	    else
	    {
	        alert("输入异常，页码范围：1到"+Math.ceil(stufflist.length/5));
	    }

	});
	//获取表头信息
	$('li').hover(function(){
	    if($(this).css("background-color") == "rgb(255, 255, 255)"){
	        $(this).css("background","rgb(255, 0, 0)");
	    }
	},function(){
	    if($(this).css("background-color") == "rgb(255, 0, 0)"){
	        $(this).css("background","rgb(255, 255, 255)");
	    }
	})
});

function showstufflist(stuff)
{
    var g_table = $("#stufftable");
    for(key in  stuff)
    {
        let thisstuff = new Array();
        let basicUnit = stuff[key].basicunit;
        thisstuff['stuffid'] = stuff[key].prodid;
        thisstuff['stuffname'] = stuff[key].prodname;
        thisstuff['batchno'] = stuff[key].batchno;
        thisstuff['amount'] = stuff[key].stockamount+basicUnit;
        thisstuff['piamount'] = stuff[key].piamount+basicUnit;
        thisstuff['detail'] = "点击查看详情";
        g_table.append(create_row(thisstuff,stuff[key].autoid));

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
        //重新增加
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

/*
 * 参数row_data：行中每个td的内容
 * 参数num，行号
 * basicUnit：基础单位
 */
function create_row(row_data,key)
{

    var row_obj = $("<tr></tr>");
    for(var k in row_data)
	{
	    if(row_data[k] == "点击查看详情")
	    {
	        let col_td = $("<td id = '"+key+"' class='mousecover'></td>");
	        col_td.html(row_data[k]);
		    row_obj.append(col_td);
	    }
	    else if(k == "autoid")
	    {
	        continue;
		}
	    else
	    {
	        let col_td = $("<td></td>");
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



function clickfunction()
{
    //页数少于10的功能
    $('.pagemin').click(function(e)
    {
        let newPage = e.target.textContent;
        if (newPage != page)
        {
            $('tbody').find('*').hide();
            showstufflist(stufflist.slice((newPage-1)*5,newPage*5));
            page = newPage;
            flashnav();
        }
    });
    //页数多于10的功能
    $('.pagelag').click(function(e)
    {
        let newPage = e.target.textContent;
        if (newPage != page)
        {
            $('tbody').find('*').hide();
            showstufflist(stufflist.slice((newPage-1)*5,newPage*5));
            page = newPage;
            flashnav();
        }
    });
    //前一页的功能
    $('.previousPage').click(function(e)
    {
        if (page != 1)
        {
            page--;
            $('tbody').find('*').hide();
            showstufflist(stufflist.slice((page-1)*5,page*5));
            flashnav();
        }
    });
    //后一页的功能
    $('.nextPage').click(function(e)
    {
        if (page != Math.ceil(stufflist.length/5))
        {
            page++;
            $('tbody').find('*').hide();
            showstufflist(stufflist.slice((page-1)*5,page*5));
            flashnav();
        }
    });
    //展开详情的功能
    $('.mousecover').click(function(e){
        let batchno = $(this).prevAll()[2].textContent;
        let stuffid = $(this).prevAll()[4].textContent;
        window.open("./productquery?autoid="+$(this).attr('id')+'&prodid='+stuffid+'&batchno='+batchno);
    });
}
