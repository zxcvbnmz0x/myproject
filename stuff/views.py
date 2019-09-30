from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Stuffrepository as sr
from menu.models import Stuffcheckin as si
from menu.models import Stuffcheckinlist as sci
from menu.models import Productstuff as ps
from menu.models import Stuffdrawpaper as sdp
from menu.models import Stuffdictionary as sd
from stuff.models import selfcont,toJSON
from django.forms.models import model_to_dict
from django.core import serializers
import json,datetime

# Create your views here.

def stuffquery(request):
    allstuff = sr.objects.all()
    return(render(request,'stuff/stuffquery.html',{
        'allstuff':json.dumps(allstuff[0].stuffname)
    }))

def findstuff(request):
    allstuff = sr.objects.all()
    return (render(request, 'stuff/findstuff.html', {
        'allstuff': json.dumps(allstuff[0].stuffname)
    }))


def showstuff(request):
    requiredict = dict()
    if request.method == 'GET' and request.is_ajax():
        for key,value in request.GET.items():
            requiredict[key] = value
        try :
            allstuff = sr.objects.filter(**requiredict).order_by("autoid")
            stuff = []
            for item in allstuff.values():
                stuff.append(toJSON(item))
            return HttpResponse(json.dumps(stuff), content_type='application/json')
        except :
            return HttpResponse(json.dumps(''), content_type='application/json')



#根据请求的内容获取数据库中对应的物料记录
def searchstuff(request):
    requiredict = dict()
    if request.method == 'GET' and request.is_ajax():
        for key,value in request.GET.items():
            requiredict[key] = value
        try :
            allstuff = sr.objects.filter(**requiredict).order_by("autoid")
            stuff = []
            for item in allstuff.values():
                stuff.append(toJSON(item))
            return HttpResponse(json.dumps(stuff), content_type='application/json')
        except :
            return HttpResponse(json.dumps(''), content_type='application/json')




def showstuffiodetail(request):
    if request.method == 'GET':
        stuffid = request.GET.get('stuffid')
        batchno = request.GET.get('batchno')
    rowitem = []

    sql = "(SELECT DATE(sci.BuyDate) piDate,sci.PiKind,scil.piAmount as inamount,0 as outamount,scil.piAmount as useamount,concat(sci.creatorid,sci.creatorname) FROM stuffcheckin sci,stuffcheckinlist scil WHERE sci.PaperNo=scil.PaperNo AND sci.PaperType = scil.PaperType AND scil.StuffID = %s AND scil.BatchNo=%s AND sci.papertype = 0 AND sci.Status > 0) \
                    UNION ALL \
						(SELECT DATE(sdp.DrawTime),'生产领料',ps.BackAmount as inamount,ps.DrawAmount as outamount,ps.BackAmount-ps.DrawAmount as useamount,concat(sdp.providerid,sdp.providername) FROM productstuff ps,stuffdrawpaper sdp WHERE ps.sdpID=sdp.autoid AND sdp.status > 1 AND ps.StuffID=%s AND ps.BatchNo = %s) \
					UNION ALL \
						(SELECT DATE(sci.BuyDate) piDate,sci.PiKind,sr.piAmount as inamount,0 as outamount,sr.piAmount as useamount,concat(sci.creatorid,sci.creatorname) FROM stuffcheckin sci,stuffcheckinlist scil,stuffrepository sr WHERE sci.PaperNo=scil.PaperNo AND sci.PaperType = scil.PaperType AND scil.StuffID = %s AND scil.BatchNo= %s AND sci.papertype = 1 AND sci.Status > 0 AND sr.ciid = scil.autoid) \
					UNION ALL \
						(SELECT DATE(sci.BuyDate) piDate,sci.PiKind,0 as inamount,scil.piamount as outamount,-scil.piamount as useamount,concat(sci.creatorid,sci.creatorname) FROM stuffcheckin sci,stuffcheckinlist scil WHERE sci.PaperNo=scil.PaperNo AND sci.PaperType = scil.PaperType AND scil.StuffID = %s AND scil.BatchNo= %s AND sci.papertype = 2 AND sci.Status > 0) \
					ORDER BY piDate "
    '''
    for item in sci.objects.raw(sql,params=[stuffid,batchno,stuffid,batchno,stuffid,batchno,stuffid,batchno]):

        rowitem.append(toJSON(item))
    print(rowitem)
    '''
    rowitem = selfcont(sql,[stuffid,batchno,stuffid,batchno,stuffid,batchno,stuffid,batchno])

    return HttpResponse(json.dumps(rowitem),content_type='application/json')

def stuffdictionary(request):
    stuffdictionary = sd.objects.all()
    stuff = []
    for item in stuffdictionary.values():
        stuff.append(toJSON(item))
    return (render(request, 'stuff/stuffdictionary.html', {
        'allstuff': stuffdictionary,
        'stuff':json.dumps(stuff)
    }))
