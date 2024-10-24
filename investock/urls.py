"""investock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from web.views import home

urlpatterns = (
    [
        path('admin/', admin.site.urls),
        path('', home.index, name='home'),
        path('login/', home.login, name='login'),
        path('logout/', home.oidc_logout, name='logout'),
        path('stock-tahu/', home.stock_tahu, name='stock_tahu'),
        path('add-stock-tahu/', home.add_tahu, name='add_tahu'),
        path('stock-barang-bumbu/', home.stock_barang_bumbu, name='stock_barang_bumbu'),
        path('add-stock-barang-bumbu/', home.add_stock_barang_bumbu, name='add_stock_barang_bumbu'),
        
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
