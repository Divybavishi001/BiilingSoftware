from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
# import datetime
import re
# Create your views here.

def dashboard(request):
    return render(request, 'index.html')

def generateorders(request):
    products = Product.objects.all().order_by('p_id')
    customer = Customer.objects.all().order_by('c_id')
    return render(request, 'generateorder.html',{'products': products,'customer': customer})

def salesorders(request):
    orders = SalesOrder.objects.all().order_by('s_id')
    return render(request, 'salesorders.html',{'orders':orders})

def customer(request):
    customers = Customer.objects.all().order_by('c_id')
    return render(request,'customer.html',{'customers': customers})

def supplier(request):
    suppliers = Supplier.objects.all().order_by('sup_id')
    return render(request, 'supplier.html',{'suppliers': suppliers})

def get_product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    data = {
        'hsn': product.p_hsncode,
        'rate': product.p_price,
        'unit':product.p_unit
    }
    return JsonResponse(data)
@csrf_exempt
@api_view(["POST"])
def add_customer(request):
    cus_name = request.data.get('c_name')
    cus_tradename = request.data.get('c_tradename')
    cus_address = request.data.get('c_address')
    cus_mobile = request.data.get('c_mobile')
    cus_gstno = request.data.get('c_gstno')
    Customer.objects.create(
        c_name=cus_name,
       c_tradename= cus_tradename,
       c_address=cus_address,
       c_mobile=cus_mobile,
       c_gstno=cus_gstno
    )
    return JsonResponse({"Status":True,"Msg":"New Customer Created successfully!!"})


@csrf_exempt
@api_view(["POST"])
def view_customer(request):
    c_id = request.data.get('c_id')
    try:
        customer = Customer.objects.get(c_id=c_id)
        response = {
            "Status": True,
            "customer": {
                "c_id": customer.c_id,
                "c_name": customer.c_name,
                "c_tradename": customer.c_tradename,
                "c_address": customer.c_address,
                "c_mobile": customer.c_mobile,
                "c_gstno": customer.c_gstno
            }
        }
    except Customer.DoesNotExist:
        response = {"Status": False, "Msg": "Customer not found"}

    return JsonResponse(response)

@csrf_exempt
@api_view(["POST"])
def edit_customer(request):
    c_id = request.data.get('c_id')
    c_name = request.data.get('c_name')
    c_tradename = request.data.get('c_tradename')
    c_address = request.data.get('c_address')
    c_mobile = request.data.get('c_mobile')
    c_gstno = request.data.get('c_gstno')

    try:
        customer = Customer.objects.get(c_id=c_id)
        customer.c_name = c_name
        customer.c_tradename = c_tradename
        customer.c_address = c_address
        customer.c_mobile = c_mobile
        customer.c_gstno = c_gstno
        customer.save()
        response = {"Status": True, "Msg": "Customer details edited successfully"}
    except Customer.DoesNotExist:
        response = {"Status": False, "Msg": "Customer not found"}

    return JsonResponse(response)

@csrf_exempt
@api_view(["POST"])
def delete_customer(request):
    c_id = request.data.get('c_id')

    try:
        customer = Customer.objects.get(c_id=c_id)
        customer.delete()
        response = {"Status": True, "Msg": "Customer deleted successfully"}
    except Customer.DoesNotExist:
        response = {"Status": False, "Msg": "Customer not found"}

    return JsonResponse(response)

@csrf_exempt
@api_view(["POST"])
def add_supplier(request):
    s_name = request.data.get('sup_name')
    s_tradename = request.data.get('sup_tradename')
    s_address = request.data.get('sup_address')
    s_mobile = request.data.get('sup_mobile')
    s_gstno = request.data.get('sup_gstno')

    Supplier.objects.create(
        sup_name=s_name,
        sup_tradename=s_tradename,
        sup_address=s_address,
        sup_mobile=s_mobile,
        sup_gstno=s_gstno
    )
    return JsonResponse({"Status":True, "Msg":"Supplier was added successfully!!"})

@csrf_exempt
@api_view(["POST"])
def view_supplier(request):
    sup_id = request.data.get('sup_id')
    try:
        supplier = Supplier.objects.get(sup_id=sup_id)
        # Assuming Supplier model fields are 'sup_id', 'sup_name', 'sup_tradename', 'sup_address', 'sup_mobile'
        response = {
            "Status": True,
            "supplier": {
                "sup_id": supplier.sup_id,
                "sup_name": supplier.sup_name,
                "sup_tradename": supplier.sup_tradename,
                "sup_address": supplier.sup_address,
                "sup_mobile": supplier.sup_mobile,
                "sup_gstno": supplier.sup_gstno
            }
        }
    except Supplier.DoesNotExist:
        response = {"Status": False, "Msg": "Supplier not found"}

    return JsonResponse(response)

@csrf_exempt
@api_view(["POST"])
def edit_supplier(request):
    s_id = request.data.get('sup_id')
    s_name = request.data.get('sup_name')
    s_tradename = request.data.get('sup_tradename')
    s_address = request.data.get('sup_address')
    s_mobile = request.data.get('sup_mobile')
    s_gstno = request.data.get('sup_gstno')

    try:
        supplier = Supplier.objects.get(sup_id=s_id)
    except:
        return JsonResponse({"Status":False,"Msg":"Supplier id not found!!"})
    
    supplier.sup_name=s_name
    supplier.sup_tradename=s_tradename
    supplier.sup_address=s_address
    supplier.sup_mobile=s_mobile
    supplier.sup_gstno=s_gstno
    supplier.save()
    return JsonResponse({"Status":True,"Msg":"Supplier deatails is updated!!"})

@csrf_exempt
@api_view(["POST"])
def delete_supplier(request):
    s_id = request.data.get('sup_id')

    try:
        supplier = Supplier.objects.get(sup_id=s_id)
    except:
        return JsonResponse({"Status":False,"Msg":"Supplier Id not found!!"})
    
    supplier.delete()
    return JsonResponse({"Status":True,"Msg":"Supplier deleted successfully!!"})

@csrf_exempt
@api_view(["POST"])
def add_purchaseorder(request):
    
    sup_id = request.data.get('sup_id')
    pur_date = datetime.strptime(data['pur_date'], '%Y-%m-%d').date()
    total_amount = request.data.get('total_amount')
    pur_products = request.data.get('pur_products', [])  # Assuming pur_products is a list of product IDs

    
    try:
        supplier = Supplier.objects.get(sup_id=sup_id)
    except Supplier.DoesNotExist:
        return JsonResponse({"Status":False,"Msg":"Supplier Id not found!!"})

    purchase_order = PurchaseOrder(
        sup_id=supplier,
        pur_date=pur_date,
        total_amount=total_amount
    )
    purchase_order.save()

    for product_id in pur_products:
        product = Product.objects.get(p_id=product_id)
        purchase_order.pur_products.add(product)

    return JsonResponse({"Status": True, "Msg": "Purchase Order added successfully!!"}, status=201)

@csrf_exempt
@api_view(["POST"])
def add_salesorder(request):
    try:
        print('runnuing......')
        invno = request.data.get('InvoiceNo')
        print('hello',invno)

        data = request.data
        
        # Create SalesOrder instance
        customer = Customer.objects.get(c_id=data['CustomerName'])
        sales_order = SalesOrder.objects.create(
            s_invoice=data['InvoiceNo'],
            s_invoicedate=data['InvoiceDate'],
            s_vehicle=data['VehicleMode'],
            s_vehicleno=data['VehicleNo'],
            s_supplydate=data['DateOSupply'],
            s_state=data['State'],
            c_id=customer,
            s_totalamount=data['TotalAmount']
        )
        
        # Create SalesOrderItems instances
        for item in data['items']:
            product = Product.objects.get(p_id=item['product'])
            SalesOrderItems.objects.create(
                s_invoice=sales_order,
                p_id=product,
                s_quantity=item['Qty']
            )
        
        return Response({"message": "Sales order created successfully."}, status=status.HTTP_201_CREATED)
    
    except Customer.DoesNotExist:
        return Response({"error": "Customer not found."}, status=status.HTTP_400_BAD_REQUEST)
    
    except Product.DoesNotExist:
        return Response({"error": "Product not found."}, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

def generate_invoice_number(request):
    if request.method == 'POST':
        invoice_date_str = request.POST.get('invoice_date')
        if not invoice_date_str:
            return JsonResponse({'error': 'Invoice date is required'}, status=400)
        try:
            invoice_date = datetime.strptime(invoice_date_str, '%Y-%m-%d').date()
        except ValueError:
            return JsonResponse({'error': 'Invalid date format'}, status=400)
        print(invoice_date)
        year = invoice_date.year
        if invoice_date.month < 4:
            financial_year_start = year - 1
            financial_year_end = year
        else:
            financial_year_start = year
            financial_year_end = year + 1

        financial_year = f"{financial_year_start}-{financial_year_end}"
        
        last_invoice = SalesOrder.objects.filter().order_by('-s_id').first()
        print(last_invoice)
        if last_invoice:
            last_number = int(last_invoice.s_invoice.split('-')[0][1:])
            new_number = last_number + 1
        else:
            new_number = 1

        invoice_number = f"A{new_number:04d}-{financial_year}"

        return JsonResponse({'invoice_number': invoice_number})

    return JsonResponse({'error': 'Invalid request method'}, status=405)