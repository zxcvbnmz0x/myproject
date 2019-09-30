from django.urls import path,include
import product.views
urlpatterns=[
    path('productquery',product.views.productquery),
    path('showproduct',product.views.showproduct),
    path('showprodiodetail',product.views.showprodiodetail),
    path('findproduct',product.views.findproduct),
    path('searchproduct',product.views.searchproduct)
]