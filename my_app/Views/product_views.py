from django.shortcuts import render, redirect, get_object_or_404
from my_app.models import Category, Product
from django.urls import reverse


def index(request):
    products = Product.objects.all()
    return render(request, "pages/products/index.html", {'products': products})


def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Product.objects.create(name=name)
        return redirect('index')  # <-- redirect to route name 'index'
    return render(request, 'pages/products/create.html')


def product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.save()
        return redirect('index')
    return render(request, 'pages/products/edit.html', {'category': category})


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('index')
