from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import logout, authenticate
from django.contrib.auth import authenticate, login as auth_login

from dash.models import Product, StockBarangBumbu


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

    return redirect('stock_tahu')

def stock_barang_bumbu(request):
    stock = StockBarangBumbu.objects.all()
    context = {
        'object_list' : stock
    }
    return render(request, 'templates/stock/bumbu.html', context=context) 

def add_stock_barang_bumbu(request):
    if request.method == "POST":
        tanggal = request.POST.get('tanggal', datetime.now())
        mamaku_masuk = request.POST.get('mamaku_masuk', 0)
        mamaku_keluar = request.POST.get('mamaku_keluar', 0)
        balado_masuk = request.POST.get('balado_masuk', 0)
        balado_keluar = request.POST.get('balado_keluar', 0)
        aida_masuk = request.POST.get('aida_masuk', 0)
        aida_keluar = request.POST.get('aida_keluar', 0)
        minyak_masuk = request.POST.get('minyak_masuk', 0)
        minyak_keluar = request.POST.get('minyak_keluar', 0)
        plastik_masuk = request.POST.get('plastik_masuk', 0)
        plastik_keluar = request.POST.get('plastik_keluar', 0)
        kresek_masuk = request.POST.get('kresek_masuk', 0)
        kresek_keluar = request.POST.get('kresek_keluar', 0)
        keterangan = request.POST.get('keterangan', '')

        mamaku_stock = int(mamaku_masuk) - int(mamaku_keluar)
        balado_stock = int(balado_masuk) - int(balado_keluar)
        aida_stock = int(aida_masuk) - int(aida_keluar)
        minyak_stock = int(minyak_masuk) - int(minyak_keluar)
        plastik_stock = int(plastik_masuk) - int(plastik_keluar)
        kresek_stock = int(kresek_masuk) - int(kresek_keluar)

        stock = StockBarangBumbu(
            mamaku_masuk=mamaku_masuk,
            mamaku_keluar=mamaku_keluar,
            mamaku_stock=mamaku_stock,
            balado_masuk=balado_masuk,
            balado_keluar=balado_keluar,
            balado_stock=balado_stock,
            aida_masuk=aida_masuk,
            aida_keluar=aida_keluar,
            aida_stock=aida_stock,
            minyak_masuk=minyak_masuk,
            minyak_keluar=minyak_keluar,
            minyak_stock=minyak_stock,
            plastik_masuk=plastik_masuk,
            plastik_keluar=plastik_keluar,
            plastik_stock=plastik_stock,
            kresek_masuk=kresek_masuk,
            kresek_keluar=kresek_keluar,
            kresek_stock=kresek_stock,
            keterangan=keterangan,
            date=tanggal
        )
        stock.save()

        messages.success(request, 'Stock berhasil ditambahkan!')
        return redirect('stock_barang_bumbu')