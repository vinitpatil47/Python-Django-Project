from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from .models import Account
from django.template import loader
import random

def home(request):
    return render(request,'createaccount/home.html')

def index(request):
    return render(request,'createaccount/create.html')
    #return HttpResponse("<h1>This is create Account Page</h1>")

class createe(CreateView):
    model = Account
   # fields = '__all__'
    fields = ['account_holder_name','address','gender','balance','mobile_number','account_type','email_id','qualification','occupation','account_status','date_of_birth','age']

def acc_info(request):
    return render(request,'createaccount/acc_info.html')

def acc_info1(request):
    template = loader.get_template('createaccount/acc_info1.html')

    try:
        obj = Account.objects.get(account_number=request.POST.get('name', ''))
    except Account.DoesNotExist:
        return render(request, 'createaccount/error.html')

    context = {'obj': obj, }
    return HttpResponse(template.render(context, request))


def dis_bal(request):
    return render(request, 'createaccount/dis_bal.html')


def dis_bal1(request):
    #name = request.POST.get('name','')
    template = loader.get_template('createaccount/dis_bal1.html')

    try:
        obj = Account.objects.get(account_number=request.POST.get('name',''))
    except Account.DoesNotExist:
        return render(request, 'createaccount/error.html')

    context={ 'obj':obj,}
    return HttpResponse(template.render(context,request))


def depo(request):
    return render(request, 'createaccount/depo.html')


def depo1(request):
    try:
        obj = Account.objects.get(account_number=request.POST.get('name', ''))
    except Account.DoesNotExist:
        return render(request, 'createaccount/error.html')

    amount=request.POST.get('amo', '')
    obj.balance = int(obj.balance) + int(amount)
    obj.save()
    return render(request,'createaccount/depo1.html')


def withdraw(request):
    return render(request, 'createaccount/withdraw.html')

def withdraw1(request):
    try:
        obj = Account.objects.get(account_number=request.POST.get('name', ''))
    except Account.DoesNotExist:
        return render(request, 'createaccount/error.html')

    amount=request.POST.get('amo', '')
    if(obj.balance >= int(amount)):
        obj.balance = int(obj.balance) - int(amount)
        obj.save()
        return render(request,'createaccount/withdraw1.html')
    return render(request, 'createaccount/error1.html')


def mon_tra(request):
    return render(request, 'createaccount/mon_tra.html')

def mon_tra1(request):
    try:
        obj1 = Account.objects.get(account_number=request.POST.get('acc1', ''))
        obj2 = Account.objects.get(account_number=request.POST.get('acc2', ''))
    except Account.DoesNotExist:
        return render(request, 'createaccount/error.html')

    if(obj2==obj1):
        return render(request, 'createaccount/error.html')

    amount=request.POST.get('amo', '')

    if(obj1.balance >= int(amount)):
        obj1.balance = int(obj1.balance) - int(amount)
        obj2.balance = int(obj2.balance) + int(amount)
        obj1.save()
        obj2.save()
        return render(request,'createaccount/mon_tra1.html')
    return render(request, 'createaccount/error1.html')

def delete(request):
    return render(request, 'createaccount/delete.html')


def delete1(request):
    #name = request.POST.get('name','')
    #template = loader.get_template('createaccount/dis_bal1.html')

    try:
        obj = Account.objects.get(account_number=request.POST.get('name','none'))
    except Account.DoesNotExist:
        return render(request, 'createaccount/error.html')

    obj.delete()
    return render(request, 'createaccount/delete1.html')


class AccountUpdate(UpdateView):
    model = Account
    fields = ['account_holder_name']
    template_name_suffix = '_update_form'
