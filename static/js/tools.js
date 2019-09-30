/*
 * 用promise异步处理ajax请求
 */
function runAsync(init_data_url,parmeters,method="GET")
{
    var toUrl ='';
    if(parmeters == '')
    {
        toUrl = init_data_url;
    }
    else
    {
        toUrl = init_data_url + '?' + parmeters;
    }
    var p = new Promise(function(resolved,reject)
	{
		//async请求是否为异步boolean
		if(method == 'GET')
		{
		    $.ajax({
		    url:toUrl,
		    type:method,
		    success:function(data)
		        {
		            resolved(data);
		        }
		    });
		}
		else if(method = 'POST')
		{
		    $.ajax({
		    url:toUrl,
		    data:parmeters,
		    type:method,
		    success:function(data)
		        {
		            resolved(data);
		        }
		});
		}
	})
		return p;
}

/*
 * 异步请求labrecords
 */
function getlabrecord(url,lrid)
{
    var p = new Promise(function(resolved,reject)
	    {
			//在这里进行处理。也许可以使用ajax
			$.get(url+'?lrid='+lrid,(data)=>{
			    //这里告诉Promise 成功了，然后去执行then方法的第一个函数
				resolved(data);
				});

		});
	return p;
}
/*
 * 获得详细货位卡信息
 */
function getdetail(url)
{
    var p = new Promise( function(resolved,reject)
	    {
			//在这里进行处理。也许可以使用ajax
			$.get(url,(data)=>{
			    //这里告诉Promise 成功了，然后去执行then方法的第一个函数
				resolved(data);
			});

		});
	return p;
}

