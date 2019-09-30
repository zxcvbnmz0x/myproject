from django.urls import path,include
import labrecord.views
urlpatterns=[
    path('getlabrecord',labrecord.views.getlabrecord)
]