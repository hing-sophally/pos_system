from django.shortcuts import render, redirect, get_object_or_404
from my_app.models import Category, Position
from django.urls import reverse


def index(request):
    position = Position.objects.all()
    return render(request, "pages/positions/index.html", {'position': position})



def position_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Position.objects.create(name=name)
        return redirect('index')  # <-- redirect to route name 'index'
    return render(request, 'pages/positions/create.html')


def position_edit(request, id):
    position = get_object_or_404(Position, id=id)
    if request.method == 'POST':
        position.name = request.POST.get('name')
        position.save()
        return redirect('index')
    return render(request, 'pages/positions/edit.html', {'position': position})


def position_delete(request, id):
    positions = get_object_or_404(Position, id=id)
    positions.delete()
    return redirect('index')
