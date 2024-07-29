from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('p_id', 'p_name', 'p_desc','p_hsncode','p_unit', 'p_price', 'quantity')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('sup_id', 'sup_name', 'sup_tradename', 'sup_address', 'sup_mobile', 'sup_gstno')

# @admin.register(PurchaseOrder)
# class PurchaseOrderAdmin(admin.ModelAdmin):
#     list_display = ('pur_id', 'sup_id', 'pur_date', 'total_amount')

# @admin.register(PurchaseOrderItems)
# class PurchaseOrderItemsAdmin(admin.ModelAdmin):
#     list_display = ('poi_id', 'pur_id', 'p_id', 'po_quantity')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('c_id', 'c_name', 'c_tradename', 'c_address', 'c_mobile', 'c_gstno')

@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ('s_id', 's_invoice','s_invoicedate','c_id', 's_date', 's_totalamount')

@admin.register(SalesOrderItems)
class SalesOrderItemsAdmin(admin.ModelAdmin):
    list_display = ('soi_id', 's_invoice', 'p_id', 's_quantity')
