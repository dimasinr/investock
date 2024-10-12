# Generated by Django 3.2.15 on 2024-10-12 13:21

import dash.helper
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0004_alter_transaction_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=dash.helper.RandomFileName('product/image/')),
        ),
    ]