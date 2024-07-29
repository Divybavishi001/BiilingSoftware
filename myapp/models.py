from django.db import models
import datetime

class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=300)
    p_desc = models.TextField(max_length=2000)
    p_hsncode = models.CharField(max_length=10,null=True)
    p_unit = models.CharField(max_length=10,null=True)
    p_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.p_name

class Supplier(models.Model):
    sup_id = models.AutoField(primary_key=True)
    sup_name = models.CharField(max_length=150)
    sup_tradename = models.CharField(max_length=200)
    sup_address = models.TextField(max_length=2000)
    sup_mobile = models.CharField(max_length=10,null=True)
    sup_gstno = models.CharField(max_length=15,null=True)

    def __str__(self):
        return str(self.sup_id)

class PurchaseOrder(models.Model):
    pur_id = models.AutoField(primary_key=True)
    sup_id = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    pur_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pur_products = models.ManyToManyField(Product, through='PurchaseOrderItems')

    def __str__(self):
        return str(self.pur_id)

class PurchaseOrderItems(models.Model):
    poi_id = models.AutoField(primary_key=True)
    pur_id = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    po_quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.poi_id)

class Customer(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=150, null=True)
    c_tradename = models.CharField(max_length=150, null=True)
    c_address = models.TextField(max_length=1000, null=True)
    c_mobile = models.CharField(max_length=10, null=True)
    c_gstno = models.CharField(max_length=15, null=True)

    def __str__(self):
        return str(self.c_id)

class SalesOrder(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_invoice = models.CharField(max_length=20, unique=True, default='DEFAULT_INVOICE')
    s_invoicedate = models.DateField(default=datetime.date.today)
    s_vehicle = models.CharField(max_length=20, null=True)
    s_vehicleno = models.CharField(max_length=20 , null=True)
    s_supplydate = models.DateField(default=datetime.date.today)
    s_state = models.CharField(max_length=50, null=True)
    c_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    s_date = models.DateField(auto_now=True)
    s_totalamount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.s_id)

class SalesOrderItems(models.Model):
    soi_id = models.AutoField(primary_key=True)
    s_invoice = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name='order_items', null=True)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    s_quantity = models.IntegerField()

    class Meta:
        unique_together = ('s_invoice', 'p_id')
