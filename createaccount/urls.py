from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #/
    path('', views.home, name='home'),

    #/createaccount
    path('createaccount', views.createe.as_view() ,name='create'),

    path('acc_info', views.acc_info, name='acc_info'),

    path('acc_info1', views.acc_info1, name='acc_info1'),

    #/display_balance
    path('dis_bal', views.dis_bal, name='dis_bal'),

    path('dis_bal1', views.dis_bal1, name='dis_bal1'),

    #deposit money
    path('depo', views.depo, name='depo'),

    path('depo1', views.depo1, name='depo1'),

    #withdraw money
    path('withdraw', views.withdraw, name='withdraw'),

    path('withdraw1', views.withdraw1, name='withdraw1'),

    #money tranfer
    path('mon_tra', views.mon_tra, name='mon_tra'),

    path('mon_tra1', views.mon_tra1, name='mon_tra1'),

    #delete object
    path('delete', views.delete, name='delete'),

    path('delete1', views.delete1, name='delete1'),

]
