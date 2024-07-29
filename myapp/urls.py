from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('generateorders/',views.generateorders,name='generateorders'),
    path('salesorders/',views.salesorders,name='salesorders'),
    path('generate_invoice_number/', views.generate_invoice_number, name='generate_invoice_number'),

    path('customer/',views.customer,name='customer'),
    path('add_customer/',views.add_customer,name='add_customer'),
    path('view_customer/',views.view_customer,name='view_customer'),
    path('edit_customer/',views.edit_customer,name='edit_customer'),
    path('delete_customer/',views.delete_customer,name='delete_customer'),

    path('supplier/',views.supplier,name='supplier'),
    path('add_supplier/',views.add_supplier,name='add_supplier'),
    path('view_supplier/',views.view_supplier,name='view_supplier'),
    path('edit_supplier/',views.edit_supplier,name='edit_supplier'),
    path('delete_supplier/',views.delete_supplier,name='delete_supplier'),
    
    path('add_purchaseorder', views.add_purchaseorder,name='add_purchaseorder'),

    path('add_salesorder/', views.add_salesorder,name='add_salesorder'),
    path('get_product_details/<int:product_id>/', views.get_product_details, name='get_product_details'),
]