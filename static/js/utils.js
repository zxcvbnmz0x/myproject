//取得整个地址栏中的参数
function getUrlparameter(flag = 0)
{
    let str = location.href;
	let num = str.indexOf("?");
	//取得所有参数   stringvar.substr(start [, length
	str=str.substr(num+1);
	if(flag == 0)
	{
	    return str;
	}
    //各个参数放到数组里
	let arr=str.split("&");
	let pararmeters = Array();
	for(var i=0;i < arr.length;i++)
	{
	    num = arr[i].indexOf("=");
	    if(num>0)
	    {
	        name = arr[i].substring(0,num);
	        value = arr[i].substr(num+1);
	        pararmeters[name] = value;
        }
        else
        {
            return false;
        }
    }
    return pararmeters;
}

//根据屏幕方式转屏
function transalewindow()
{
	if(window.orientation==90||window.orientation==-90){
		transform: rotate(90);
	}

	addEventListener('load', function(){
	    checkOrient();
	    window.onorientationchange = checkOrient;
	});
}

function checkOrient() {
        //landscape是横向，portrait是纵向
	    if (window.orientation == 0 || window.orientation == 180){
	        var screenOrientation = 'portrait';
	    }
	    else if (window.orientation == 90 || window.orientation == -90){
	        var screenOrientation = 'landscape';
	    }
	    return screenOrientation;
	}