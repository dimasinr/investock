import uuid
from django.db import models

from dash.helper import RandomFileName

class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=RandomFileName('product/image/'), null=True, blank=True)
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
    quantity = models.BigIntegerField(default=0)
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
    mamaku_masuk = models.BigIntegerField(default=0)
    mamaku_keluar = models.BigIntegerField(default=0)
    mamaku_stock = models.BigIntegerField(default=0)
    balado_masuk = models.BigIntegerField(default=0)
    balado_keluar = models.BigIntegerField(default=0)
    balado_stock = models.BigIntegerField(default=0)
    aida_masuk = models.BigIntegerField(default=0)
    aida_keluar = models.BigIntegerField(default=0)
    aida_stock = models.BigIntegerField(default=0)
    minyak_masuk = models.BigIntegerField(default=0)
    minyak_keluar = models.BigIntegerField(default=0)
    minyak_stock = models.BigIntegerField(default=0)
    plastik_masuk = models.BigIntegerField(default=0)
    plastik_keluar = models.BigIntegerField(default=0)
    plastik_stock = models.BigIntegerField(default=0)
    kresek_masuk = models.BigIntegerField(default=0)
    kresek_keluar = models.BigIntegerField(default=0)
    kresek_stock = models.BigIntegerField(default=0)
    keterangan = models.TextField(blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'stock_bumbu'

    def __str__(self):
        return f"Transaksi ID : {self.stock_id}"


class RekapStockBarang(models.Model):
    rekap_id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(null=True, blank=True)
    jenis_barang = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    pesanan = models.BigIntegerField(default=0, null=True, blank=True)
    masuk = models.BigIntegerField(default=0, null=True, blank=True)
    stock = models.BigIntegerField(default=0, null=True, blank=True)
    barang_keluar = models.BigIntegerField(default=0, null=True, blank=True)
    sisa_gudang = models.BigIntegerField(default=0, null=True, blank=True)
    terjual = models.BigIntegerField(default=0, null=True, blank=True)
    sisa = models.BigIntegerField(default=0, null=True, blank=True)
    sisa_akhir = models.BigIntegerField(default=0, null=True, blank=True)
    keterangan = models.TextField(blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'rekap_stock_barang'

    def __str__(self):
        return f"Transaksi ID : {self.rekap_id}"
