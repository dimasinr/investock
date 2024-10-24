import uuid
from django.db import models

from dash.helper import RandomFileName

class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=RandomFileName('product/image/'), null=True, blank=True)
    price = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    class Meta:
        managed = True  
        db_table = 'product'

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'employee'

    def __str__(self):
        return self.name


class Transaction(models.Model):
    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seller = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    produk = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        managed = True  
        db_table = 'transaction'

    def __str__(self):
        return f"Transaksi ID : {self.transaction_id} - Produk : {self.produk.name}"


class Bumbu(models.Model):
    bumbu_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = True  
        db_table = 'bumbu'

    def __str__(self):
        return self.name
    
class StockBarangBumbu(models.Model):
    stock_id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(null=True, blank=True)
    mamaku_masuk = models.PositiveIntegerField(default=0)
    mamaku_keluar = models.PositiveIntegerField(default=0)
    mamaku_stock = models.PositiveIntegerField(default=0)
    balado_masuk = models.PositiveIntegerField(default=0)
    balado_keluar = models.PositiveIntegerField(default=0)
    balado_stock = models.PositiveIntegerField(default=0)
    aida_masuk = models.PositiveIntegerField(default=0)
    aida_keluar = models.PositiveIntegerField(default=0)
    aida_stock = models.PositiveIntegerField(default=0)
    minyak_masuk = models.PositiveIntegerField(default=0)
    minyak_keluar = models.PositiveIntegerField(default=0)
    minyak_stock = models.PositiveIntegerField(default=0)
    plastik_masuk = models.PositiveIntegerField(default=0)
    plastik_keluar = models.PositiveIntegerField(default=0)
    plastik_stock = models.PositiveIntegerField(default=0)
    kresek_masuk = models.PositiveIntegerField(default=0)
    kresek_keluar = models.PositiveIntegerField(default=0)
    kresek_stock = models.PositiveIntegerField(default=0)
    keterangan = models.TextField(blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'stock_bumbu'

    def __str__(self):
        return f"Transaksi ID : {self.stock_id}"
