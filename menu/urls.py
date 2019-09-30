from django.urls import path,include
import menu.views
urlpatterns=[
    path('hello', menu.views.hello),
    path('',menu.views.menu),

]
