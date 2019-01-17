from django.shortcuts import render
from django.template.response import TemplateResponse
from .utils import get_customer_data, get_details, get_customer_order_count

def upload_data(request):
    order_count, amount, customer_order_count = get_customer_data()
    ordered_once, ordered_twice, ordered_thrice, ordered_fourtimes, ordered_higher = get_customer_order_count(
    																			customer_order_count) 		
    customer_order_count = sorted(customer_order_count.items(), key = lambda x:x[1])
    ctx = {
        'customer_order_count':customer_order_count,
    	'order_count':order_count,
    	'amount':amount,
    	'ordered_once' : ordered_once
    }
    return TemplateResponse(request, 'customer/list.html', ctx)