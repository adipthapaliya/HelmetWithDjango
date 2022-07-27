from django.shortcuts import render, redirect
from product.form import ProductForm, UpdateForm
from product.models import ProductModel,UserCartModel,BuyProductModel
from django.contrib.auth.decorators import login_required


# Create your views here.

def add (request):
    data = ProductForm(request.POST, request.FILES)
    data.save()

    return redirect('/admin/addproduct') 

def delete(request,id):
    data = ProductModel.objects.get(id=id)
    data.delete()
    return redirect('/admin/shop')  

def update(request,id):

    if request.method == 'POST' :
        value = ProductModel.objects.get(id=id)
        data = UpdateForm(request.POST, request.FILES,instance=value)
        data.save()
        return redirect('/admin/shop')

    else:
        data = ProductModel.objects.get(id=id)
        return render(request,'mainuser/add.html',{'product':data})


@login_required(login_url='/login')
def addtocart(request,id,uid):
    data =  UserCartModel(product_id=id, user_id=uid )
    data.save()

    cart = UserCartModel.objects.filter(user_id=id)
    url_id = "/cart/%s"%(uid)


    return redirect(url_id)

@login_required(login_url='/login')
def  buy(request,id,uid):
    data =  BuyProductModel(product_id=id, user_id=uid )
    data.save()

    url_id = "/purchase/%s"%(uid)
    return redirect(url_id)

    


@login_required(login_url='/login')

def deletecart(request,id,uid):
        data = UserCartModel.objects.filter(product_id=id,user_id=uid)
        data.delete()

        url_id = "/cart/%s"%(uid)
        return redirect(url_id)


@login_required(login_url='/login')
def  delivered(request,id,uid):
    data =  BuyProductModel.objects.get(product_id=id, user_id=uid )
    data.delete()

    return redirect('/admin/order')
