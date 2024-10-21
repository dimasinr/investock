from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import logout, authenticate
from django.contrib.auth import authenticate, login as auth_login

from dash.models import Product


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  
            messages.success(request, 'Login Berhasil')
            return redirect('home') 
        else:
            messages.error(request, 'Username atau password salah')  
            return redirect('login') 
    return render(request, 'templates/auth/login.html')

def index(request):
    if request.user.is_authenticated:
        return render(request, 'templates/home/index.html')
    else:
        return redirect('login')
    
def oidc_logout(request):
    logout(request)  
    return redirect('login') 

def stock_tahu(request):
    product = Product.objects.all().order_by('name')
    context = {
        'object_list' : product
    }
    return render(request, 'templates/stock/tahu.html', context=context)

def add_tahu(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        harga = request.POST.get('harga')
        berat = request.POST.get('berat')
        stock = request.POST.get('stock')

        new_tahu = Product(
            name=name,
            price=harga,
            weight=berat,
            stock=stock,
        )
        new_tahu.save() 

        messages.success(request, 'Stock berhasil ditambahkan!')
        return redirect('stock_tahu')

    return render(request, 'templates/tahu/add.html') 