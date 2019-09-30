from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Clerks,Menu
import json
# Create your views here.
def hello(response):
    '''
    all_clerks = Clerks.objects.all()
    clerkname = all_clerks[0].clerksname
    return HttpResponse(clerkname)
    '''
    return HttpResponse('this is menu hello')

def menu(request):
    all_menu = Menu.objects.all()
    first_menu = {}
    second_menu = {}
    List = {}
    for item in all_menu:
        if item.parent_article_id == 0:
            first_menu[item.autoid] = item.article
        else:
            second_menu[item.article] = {item.parent_article_id:item.url}
            List[item.article] = item.url

    return render(request,'menu/menu.html',{
                    'first_menu':first_menu,
                    'second_menu':second_menu,
                    'List':json.dumps(List)
    })

def index(request):

    return render(request,'menu/index.html',{
    })
