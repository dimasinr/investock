from django.contrib import admin
from .models import Employee, Product, Transaction
from import_export.admin import ImportExportModelAdmin

@admin.register(Employee, site=admin.site)
class EmployeeAdmin(ImportExportModelAdmin):
    list_display = ('employee_id', 'name', 'city', 'phone_number', 'address')
    search_fields = ('name',)  
    ordering = ('name',)

@admin.register(Product, site=admin.site)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('product_id', 'name', 'price', 'weight', 'stock', 'date')
    search_fields = ('name',)  
    ordering = ('product_id',)

@admin.register(Transaction, site=admin.site)
class TransactionAdmin(ImportExportModelAdmin):
    list_display = ('transaction_id', 'produk', 'seller', 'quantity', 'date')
    search_fields = ('produk__name', 'seller__name') 
    ordering = ('transaction_id',)
