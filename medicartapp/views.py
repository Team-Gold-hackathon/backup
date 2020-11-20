from django.shortcuts import render, redirect
from .models import *
from .forms  import OrderForm, CreateUserForm, CustomerForm
from django.forms import inlineformset_factory
# Create your views here.
#from .filters import OrderFilter
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group


def home(request):
    return render(request, 'medicartapp/home.html')

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username =  form.cleaned_data.get('username')
            messages.success(request, 'Account was created for'+username)
            return redirect('home')
    
    context = {'form':form}
    return render(request, "medicartapp/register.html", context)
    
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password )

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'User or Password is incorrect')
    context = {}
    return render(request, "medicartapp/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')

#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin', 'pharmacy'])
def products(request):
    products=Product.objects.all()
    context ={'products': products}
    return render(request, 'medicartapp/products.html',context)

#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin', 'pharmacy'])
def PersonalCare(request):
    products=Product.objects.all()
    context ={'products': products}
    return render(request, 'medicartapp/products.html',context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# def customer(request, pk):
#     customer=Customer.objects.get(id=pk)
#     orders = customer.order_set.all()
#     order_count = orders.count()
#     context = {'customer':customer, 'orders':orders, 'order_count':order_count}
#     return render(request, 'medicartapp/customer.html', context)