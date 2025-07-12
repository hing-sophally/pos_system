from django.shortcuts import render, redirect, get_object_or_404
from my_app.models import Category
from django.urls import reverse


def index(request):
    categories = Category.objects.all()
    return render(request, "pages/categories/index.html", {'categories': categories})


def category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('index')  # <-- redirect to route name 'index'
    return render(request, 'pages/categories/create.html')


def category_edit(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.save()
        return redirect('index')
    return render(request, 'pages/categories/edit.html', {'category': category})


def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('index')
