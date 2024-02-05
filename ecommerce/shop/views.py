from django.shortcuts import render,redirect
from shop.models import Category
from shop.models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def allcategories(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})

def allproducts(request,p):
    c=Category.objects.get(name=p)
    p=Product.objects.filter(category=c)
    return render(request,'product.html',{'c':c,'p':p})

def details(request,p):
    pd=Product.objects.get(name=p)
    return render(request,'detail.html',{'pd':pd})

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        fname=request.POST['f']
        lname=request.POST['l']
        e=request.POST['e']
        if(p==cp):
            u=User.objects.create_user(username=u,password=p,first_name=fname,last_name=lname,email=e)
            u.save()
            return redirect('shop:login')
        else:
            return HttpResponse("Passwords are not same")
    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
        else:
            return HttpResponse("Invalid credentials")
    return render(request,'login.html')

@login_required()
def user_logout(request):
    logout(request)
    # return HttpResponse("Logout")
    return redirect('shop:login')
