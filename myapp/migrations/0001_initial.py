# Generated by Django 5.0.7 on 2024-07-24 10:37

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=150, null=True)),
                ('c_tradename', models.CharField(max_length=150, null=True)),
                ('c_address', models.TextField(max_length=1000, null=True)),
                ('c_mobile', models.CharField(max_length=10, null=True)),
                ('c_gstno', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=300)),
                ('p_desc', models.TextField(max_length=2000)),
                ('p_hsncode', models.CharField(max_length=10, null=True)),
                ('p_unit', models.CharField(max_length=10, null=True)),
                ('p_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('pur_id', models.AutoField(primary_key=True, serialize=False)),
                ('pur_date', models.DateField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('sup_id', models.AutoField(primary_key=True, serialize=False)),
                ('sup_name', models.CharField(max_length=150)),
                ('sup_tradename', models.CharField(max_length=200)),
                ('sup_address', models.TextField(max_length=2000)),
                ('sup_mobile', models.CharField(max_length=10, null=True)),
                ('sup_gstno', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderItems',
            fields=[
                ('poi_id', models.AutoField(primary_key=True, serialize=False)),
                ('po_quantity', models.IntegerField(default=1)),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('pur_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.purchaseorder')),
            ],
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='pur_products',
            field=models.ManyToManyField(through='myapp.PurchaseOrderItems', to='myapp.product'),
        ),
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_invoice', models.CharField(default='DEFAULT_INVOICE', max_length=20, unique=True)),
                ('s_invoicedate', models.DateField(default=datetime.date.today)),
                ('s_vehicle', models.CharField(max_length=20, null=True)),
                ('s_vehicleno', models.CharField(max_length=20, null=True)),
                ('s_supplydate', models.DateField(default=datetime.date.today)),
                ('s_state', models.CharField(max_length=50, null=True)),
                ('s_date', models.DateField(auto_now=True)),
                ('s_totalamount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('c_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
            ],
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='sup_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.supplier'),
        ),
        migrations.CreateModel(
            name='SalesOrderItems',
            fields=[
                ('soi_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_quantity', models.IntegerField()),
                ('p_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('s_invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='myapp.salesorder')),
            ],
            options={
                'unique_together': {('s_invoice', 'p_id')},
            },
        ),
    ]
