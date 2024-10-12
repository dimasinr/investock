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
        managed = True  # Atau hapus baris ini jika ingin menggunakan managed=False
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
        managed = True  # Atau hapus baris ini jika ingin menggunakan managed=False
        db_table = 'employee'

    def __str__(self):
        return self.name


class Transaction(models.Model):
    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    produk = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    seller = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        managed = True  # Atau hapus baris ini jika ingin menggunakan managed=False
        db_table = 'transaction'

    def __str__(self):
        return f"Transaksi ID : {self.transaction_id} - Produk : {self.produk.name} - Seller : {self.seller.name}"
