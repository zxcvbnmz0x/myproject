from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Labrecords
from django.core import serializers
from labrecord.models import Tools
import json
# Create your views here.

def getlabrecord(request):
    if request.method == 'GET':
        lrid = request.GET.get('lrid')
        chktype = request.GET.get('chktype',default= 'not set' )
        labtype = request.GET.get('labtype',default= -1 )

    if chktype == 'not set' and labtype == -1:
        labitem = Labrecords.objects.filter(autoid=int(lrid));
    else:
        labitem = Labrecords.objects.filter(ciid=lrid,labtype=labtype)
    return HttpResponse(serializers.serialize('json',labitem),content_type="application/json")