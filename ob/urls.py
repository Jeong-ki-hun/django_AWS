from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('map/',views.map, name='map'),
    path('shop/congestion/', views.index, name='index'),
    path('shop/', views.shop_list, name='shop_list'),
    path('shop/dash/',views.Dashborad, name='dash')
    # ex: /polls/5/
    ]