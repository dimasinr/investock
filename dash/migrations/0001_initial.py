# Generated by Django 3.2.15 on 2024-10-12 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('address', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField(default=0)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'product',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('produk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dash.product')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dash.employee')),
            ],
            options={
                'db_table': 'transaction',
                'managed': True,
            },
        ),
    ]
