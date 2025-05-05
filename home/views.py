from django.shortcuts import render
from .models import Product, Contact
# Create your views here.

def navProducts():
    return Product.objects.all()

def index(request):
    navproducts = navProducts()
    home_products = Product.objects.all()[:8]
    context = {
        'navproducts': navproducts,
        'home_products':home_products
    }
    return render(request, 'home/index.html', context)

def about(request):
    navproducts = navProducts()
    context = {
        'navproducts': navproducts
    }
    return render(request, 'home/about.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
    navproducts = navProducts()
    context = {
        'navproducts': navproducts
    }
    return render(request, 'home/contact.html', context)

def products(request):
    navproducts = navProducts()
    products = Product.objects.all()
    context = {
        'navproducts': navproducts,
        'products':products
    }
    return render(request, 'home/products.html', context)

def products_detail(request, slug):
    navproducts = navProducts()
    product = Product.objects.get(slug=slug)
    context = {
        'navproducts': navproducts,
        'product':product
    }
    return render(request, 'home/products_detail.html', context)

def termandcondition(request):
    navproducts = navProducts()
    context = {
        'navproducts': navproducts
    }
    return render(request, 'home/termandcondition.html', context)

def cancellationandrefund(request):
    navproducts = navProducts()
    context = {
        'navproducts': navproducts
    }
    return render(request, 'home/cancellationandrefund.html', context)

def privacyandpolicy(request):
    navproducts = navProducts()
    context = {
        'navproducts': navproducts
    }
    return render(request, 'home/privacyandpolicy.html', context)

def shippinganddelivery(request):
    navproducts = navproducts()
    context = {
        'navproducts': navproducts
    }
    return render(request, 'home/shippinganddelivery.html', context)