$(function(){
var dataArr={
    "data":[
        {"id":1,"name":"2019-1","data":"10"},
        {"id":2,"name":"2019-2","data":"20"},
        {"id":3,"name":"2019-3","data":"10"},
        {"id":4,"name":"2019-4","data":"44"},
        {"id":5,"name":"2019-5","data":"50"},
        {"id":6,"name":"2019-6","data":"69"},
        {"id":7,"name":"2019-7","data":"72"},
        {"id":8,"name":"2019-8","data":"88"},
        {"id":9,"name":"2019-9","data":"92"},
        {"id":10,"name":"2019-10","data":"15"},
        {"id":11,"name":"2019-11","data":"10"}
    ]
};
data_x = [];
data_y = [];

for(var key in dataArr)
{
    new histogram(dataArr[key]);
}

});




function histogram(data)
{
    var data_X,data_Y,data_BG = [];

    var bgColor=new Array("#666666","#21AA7C","#2277BB","#dc7644","#BBAA22","#AA22AA","#338800","#1099EE","#ffcc33","#ED3810");
    data.forEach(function(element,index){
        data_X[index] = element.name;
        data_Y[index] = element.data;
    })
    console.log(data_X);
    controls = setControls();
    buildHtml_X(data_X,controls.histogramX);
    buildHtml_Y(data_Y,controls.histogramY);
    buildHtml_BG(data_BG,controls.histogramBG);
}
//初始化X、Y和背景的jquery对象
    function setControls()
    {
        var controls={};
        controls.histogramContainer=$("#histogram-container");
        controls.histogramX=controls.histogramContainer.children("div.histogram-x");
        controls.histogramY=controls.histogramContainer.children("div.histogram-y");
        controls.histogramBG=controls.histogramContainer.children("div.histogram-background");
        return controls;
    }
    //初始化X轴
    function buildHtml_X(data,y)
    {

    }
    //初始化Y轴
    function buildHtml_Y(data,y)
    {

    }
    //初始化背景
    function buildHtml_BG(data,y)
    {

    }


