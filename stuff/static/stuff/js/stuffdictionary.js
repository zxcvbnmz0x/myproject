
//	    var testdata = testdata;
//stuff从Django传递过来的所有物料
$(function(){

$("table > tbody").append(showstuff(stuff));
flashclickfunction();


$("button").click(function(){
    var text = $(this).text();
    switch(text)
    {
        case "全部":displaystuff(stuff);break;
        case "主材料":displaystuff(stuff,0);break;
        case "辅材料":displaystuff(stuff,1);break;
        case "内包材":displaystuff(stuff,2);break;
        case "外包材":displaystuff(stuff,3);break;

    }

})


//console.log(allstuff);
})

function displaystuff(stuff,flag =-1)
{
    let thisstuff = new Array();
    if(flag != -1)
    {
        stuff.forEach(function(vals,index){

            if(vals.stufftype == flag)
            {
                thisstuff.push(vals);
            }
        })
    }
    else{thisstuff = stuff;}
    $("table > tbody >").find('*').hide();
    $("table > tbody").append(showstuff(thisstuff));
    flashclickfunction();
}

function showstuff(stuff)
{
    let htmltext =  "";
    stuff.forEach(function(vals,index){
        let content = "<tr value =" + index +"><td>"+ vals.stuffid +"</td><td>"+ vals.stuffname +"</td><td>"+ vals.kind +"</td><td>"+ vals.spec +"</td><td>"+ vals.package +"</td><td>"+ vals.allowno +"</td><td>"+ vals.storage +"</td></tr>";
        htmltext = htmltext + content;
    })
    return htmltext;
}
function flashclickfunction()
{
    $("tbody > tr").click(function(){
    let index = $(this).attr("value");
    selectstuff = stuff[index];
    displaydetail(selectstuff);
})
}

function displaydetail(stuff = 0)
{
    $("#detail").css("display",'block');
    $(".close").click(function(){
        $("#detail")
        $("#detail").css("display",'none');


    })


}