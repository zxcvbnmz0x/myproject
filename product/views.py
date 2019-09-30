from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Producingplan as pp
from menu.models import Productrepository as pr
from django.core import serializers
from product.models import selfcont,toJSON
import json
# Create your views here.

#货位卡详细出入记录页面
def productquery(request):
    allproductlist = pp.objects.all()
    return(render(request,'product/productquery.html',{
        'allproductlist':json.dumps(allproductlist[0].prodname)
    }))

#对应的产品出入库记录
def findproduct(request):
    allstuff = pr.objects.all()
    return (render(request, 'product/findproduct.html', {
        'allstuff': json.dumps(allstuff[0].prodname)
    }))

#获得请求对应的产品
def searchproduct(request):
    requiredict = dict()
    if request.method == 'GET' and request.is_ajax():

        for key,value in request.GET.items():
            requiredict[key] = value

        try :
            allstuff = pr.objects.filter(**requiredict).order_by("autoid")
            stuff = []
            for item in allstuff.values():
                stuff.append(toJSON(item))
            return HttpResponse(json.dumps(stuff), content_type='application/json')
        except :
            return HttpResponse(json.dumps(''), content_type='application/json')



def showproduct(request):
    if request.method == 'GET':
        position = request.GET.get('position')
    allproduct = pr.objects.filter(position=position)

    return HttpResponse(serializers.serialize("json",allproduct), content_type='application/json')



def showprodiodetail(request):
    if request.method == 'GET':
        prodid = request.GET.get('prodid')
        batchno = request.GET.get('batchno')
        ppid = request.GET.get('ppid')
    rowitem = []

    sql = "(SELECT piDate as piDate,'生产入库' as source,piAmount as inamount,0 as outamount,position as position,piAmount as useamount,concat(dpWarehousemanID,dpWarehousemanName) as operator FROM productputinnotes WHERE ppid = %s) \
            UNION ALL \
                    (SELECT DATE(pcp.PutInTime) as piDate,pcp.pikind as source,pcd.amount as inamount,0 as outamount,pcd.location as position,pcd.amount as useamount,concat(pcp.deptid,pcp.deptname) FROM productcheckinpaper pcp,productcheckindata pcd WHERE pcd.pcipID=pcp.autoid AND pcd.dictID=%s AND pcd.BatchNo = %s) \
			UNION ALL \
                (SELECT DATE(ppop.PutOutTime) as piDate,ppop.pokind as source,0 as inamount,ppod.amount as outamount,' ' as position,-ppod.amount as useamount,concat(ppop.AuditorID,ppop.AuditorName) FROM productputoutpaper ppop,productputoutdata ppod WHERE ppod.ppopid=ppop.autoid AND ppod.dictid = %s AND ppod.batchno = %s) \
			UNION ALL \
				(SELECT pw.wDate as piDate,'产品退库' as source,sum(pwg.amount) as inamount,0 as outamount,ps.position as position,sum(pwg.amount) as useamount,concat(ps.WarehousemanID,ps.WarehousemanName) FROM productrepository ps,pwngoods pwg,productwithdrawnotes pw WHERE pwg.pwnid=pw.autoid AND pwg.prodid = %s AND pwg.batchno = %s AND ps.prodid = %s AND ps.batchno = %s having SUM(pwg.amount)>0) \
			UNION ALL \
                (SELECT sg.saledate as piDate,'销售发货' as source,0 as inamount,sum(sg.saleamount) as outamount,sn.clientname as position,-sum(saleamount) as useamount,concat(sn.consignmentid,sn.consignmentname) FROM salesgoods sg,salesnotes sn WHERE sg.snid = sn.autoid and sg.prodid = %s and sg.batchno = %s) \
			ORDER BY piDate "

    rowitem = selfcont(sql, [ppid,prodid, batchno, prodid, batchno, prodid, batchno, prodid, batchno, prodid, batchno])

    return HttpResponse(json.dumps(rowitem), content_type='application/json')