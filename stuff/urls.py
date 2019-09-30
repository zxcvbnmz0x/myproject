from django.urls import include,path
import stuff.views
urlpatterns=[
    path('stuffquery',stuff.views.stuffquery),
    path('showstuff',stuff.views.showstuff),
    path('showstuffiodetail',stuff.views.showstuffiodetail),
    path('findstuff',stuff.views.findstuff),
    path('searchstuff',stuff.views.searchstuff),
    path('stuffdictionary',stuff.views.stuffdictionary)
]