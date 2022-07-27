from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log
from django.contrib.auth import logout

from product.models import ProductModel,BuyProductModel
from user.models import MessageModel

# Create your views here.

@login_required(login_url='/admin/login')
def index(request):
    return render(request,'mainuser/index.html')

@login_required(login_url='/admin/login')
def addproduct(request):
    return render(request,'mainuser/add.html')

@login_required(login_url='/admin/login')
def editproduct(request,id):
    data = ProductModel.objects.get(id=id)

    return render(request,'mainuser/add.html',{'product':data})


@login_required(login_url='/admin/login')
def nike(request):
    nike = ProductModel.objects.all().filter(product_category='nike')

    return render(request,'mainuser/nike.html',{'nike':nike})


@login_required(login_url='/admin/login')
def adidas(request):
    adidas = ProductModel.objects.all().filter(product_category='adidas')

    return render(request,'mainuser/adidas.html',{'adidas':adidas})


@login_required(login_url='/admin/login')
def converse(request):
    converse = ProductModel.objects.all().filter(product_category='converse')

    return render(request,'mainuser/converse.html',{'converse':converse})


@login_required(login_url='/admin/login')
def puma(request):
    puma = ProductModel.objects.all().filter(product_category='puma')

    return render(request,'mainuser/puma.html',{'puma':puma})


@login_required(login_url='/admin/login')

def order(request):
    
    order = BuyProductModel.objects.select_related('product','user')
    
    return render(request,'mainuser/order.html',{'order':order})

@login_required(login_url='/admin')
def message(request):
    message = MessageModel.objects.all()
    return render(request,'mainuser/message.html',{'message':message})

def login(request):
    return render(request,'login_register/adminlogin.html')

def verification(request):
        username= request.POST['username']
        password= request.POST['password']

        user = authenticate(request,username=username, password=password)

        
        if user is not None:
            log(request,user)

            if user.is_superuser == 1:

                return redirect('/admin')

            else:
                logout(request)
                return redirect('/admin/login')

        else:
            return redirect('/admin/login')

def log_out(request):
    logout(request)
    return redirect('/admin/login')