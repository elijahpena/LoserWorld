from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'order'

urlpatterns = [
        path('', views.orderView, name='order')
        ]
