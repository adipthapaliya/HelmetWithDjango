from django.shortcuts import render,redirect
from user.form import MessageForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from product.models import ProductModel, UserCartModel, BuyProductModel


# Create your views here.


def index(request):
    return render(request,'user/index.html')

def about(request):
    return render(request,'user/about.html')

def contact(request):
    return render(request,'user/contact.html')


def message(request):
    data = MessageForm(request.POST)
    data.save()

    return redirect('/contact') 


def nike(request):
    nike = ProductModel.objects.all().filter(product_category='nike')

    return render(request,'user/nike.html',{'nike':nike})


def adidas(request):
    adidas = ProductModel.objects.all().filter(product_category='adidas')

    return render(request,'user/adidas.html',{'adidas':adidas})


def converse(request):
    converse = ProductModel.objects.all().filter(product_category='converse')

    return render(request,'user/converse.html',{'converse':converse})


def puma(request):
    puma = ProductModel.objects.all().filter(product_category='puma')

    return render(request,'user/puma.html',{'puma':puma})

def details(request,id):
    data = ProductModel.objects.get(id=id)
    return render(request,'user/details.html',{'data':data})


def cart(request,id):

    cart = UserCartModel.objects.filter(user_id=id)
    item = ProductModel.objects.all()

    return render(request,'user/cart.html',{'cart':cart,'item':item})

def purchase(request,id):

    cart =  BuyProductModel.objects.filter(user_id=id)
    item = ProductModel.objects.all()

    return render(request,'user/purchase.html',{'cart':cart,'item':item})


def login(request):
    return render(request,'login_register/login.html')

def register(request):
    return render(request,'login_register/register.html')

def createuser(request):
    if request.method == "POST":

        if request.POST['password']==request.POST['cpassword']:
            User.objects.create_user(
                first_name = request.POST['fname'],
                username = request.POST['username'],
                password = request.POST['password'],
                email = request.POST['email'],

            )
            return redirect('/login')

        else:

            return redirect('/register')



    else:   
        return redirect('/register')


def verification(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']    
        
        user = authenticate(request,username=username, password=password)

        if user is not None:
            log(request,user)

            if user.is_superuser == 0:
                return redirect('/')

            else:
                logout(request)

                return redirect("/login")


        else:
            return redirect("/login")

    else:
            return redirect("/login")


def log_out(request):
    logout(request)
    return redirect('/')