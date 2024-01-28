from django.shortcuts import render
from django.http import HttpResponse


def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''

    return HttpResponse('Welcome to 6410742529 Sira Insan views!')

def item_view(request, item_id):
 context_data = {
 "item_id": item_id
 }
 return render(request, 'index.html',context = context_data)

def home_page_view(request):
    context_data = {
        "page_title": "Home Page",
        
    }
    return render(request, 'home.html', context=context_data)

def category_page_view(request):
    context_data = {
        "page_title": "Category Page",
        
    }
    return render(request, 'category.html', context=context_data)

def product_page_view(request):
    context_data = {
        "page_title": "Product Page",
        
    }
    return render(request, 'product.html', context=context_data)

def checkout_page_view(request):
    context_data = {
        "page_title": "Checkout Page",
        
    }
    return render(request, 'checkout.html', context=context_data)

def contact_page_view(request):
    context_data = {
        "page_title": "Contact Page",
        
    }
    return render(request, 'contact.html', context=context_data)