from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_actions, name='all_actions'),
    path('<str:shop>', views.shop_actions, name='shop_actions'),
]