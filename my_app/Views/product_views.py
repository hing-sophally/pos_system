import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from my_app.models import Category, Product

@login_required

def index(request):
    products = Product.objects.all()
    return render(request, "pages/products/index.html", {"products": products})

@login_required

def show(request):
    categories = Category.objects.all()
    return render(request, 'pages/products/create.html', {"categories": categories})

@login_required

def product_create(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        barcode = request.POST.get('barcode')
        sale_price = request.POST.get('sale_price')
        unit_stock = request.POST.get('stock')
        category_id = request.POST.get('category_id')
        photo = request.FILES.get('photo')

        Product.objects.create(
            name=name,
            barcode=barcode,
            sale_price=sale_price,
            unit_stock=unit_stock,
            category_id=category_id,
            photo=photo
        )
        return redirect('index_product')  # ← redirect to /product/index/

    return render(request, 'pages/products/create.html', {"categories": categories})



@login_required

def product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    categories = Category.objects.all()

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.barcode = request.POST.get('barcode')
        product.sale_price = request.POST.get('sale_price')
        product.unit_stock = request.POST.get('stock')
        product.category_id = request.POST.get('category_id')

        # Check if new photo uploaded
        if 'photo' in request.FILES:
            new_photo = request.FILES['photo']

            # Delete old photo if exists
            if product.photo:
                old_path = os.path.join(settings.MEDIA_ROOT, str(product.photo))
                if os.path.exists(old_path):
                    os.remove(old_path)

            # Replace with new photo
            product.photo = new_photo

        product.save()
        return redirect('index_product')

    return render(request, 'pages/products/edit.html', {'product': product, 'categories': categories})

@login_required

def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('index_product')  # ← redirect to /product/index/
