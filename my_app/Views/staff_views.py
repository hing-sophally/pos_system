import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from my_app.models import Category, Product, Staff, Position

@login_required

def index(request):
    positions = Position.objects.all()
    staffs = Staff.objects.all()
    return render(request, "pages/staffs/index.html", {"staffs": staffs , "positions": positions})

@login_required

def show(request):
    positions = Position.objects.all()
    staffs = Staff.objects.all()
    return render(request, 'pages/staffs/create.html', {"staffs": staffs , "positions": positions})

@login_required

def staff_create(request):
    staffs = Staff.objects.all()
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        position = request.POST.get('position')
        photo = request.FILES.get('photo')
        position_id = request.POST.get('position_id')
        Staff.objects.create(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            date_of_birth=date_of_birth,
            position=position,
            position_id=position_id,
            photo=photo,
        )
        return redirect('index_staff')  # ← redirect to /product/index/

    return render(request, 'pages/products/create.html', {"staffs": staffs})



@login_required

def staff_edit(request, id):
    staffs = get_object_or_404(Staff, id=id)
    positions = Position.objects.all()

    if request.method == 'POST':
        staffs.first_name = request.POST.get('first_name')
        staffs.last_name = request.POST.get('last_name')
        staffs.gender = request.POST.get('gender')
        staffs.date_of_birth = request.POST.get('date_of_birth')
        staffs.position = request.POST.get('position')
        staffs.photo = request.FILES.get('photo')
        staffs.position = request.POST.get('position_id')
        # Check if new photo uploaded
        if 'photo' in request.FILES:
            new_photo = request.FILES['photo']

            # Delete old photo if exists
            if staffs.photo:
                old_path = os.path.join(settings.MEDIA_ROOT, str(staffs.photo))
                if os.path.exists(old_path):
                    os.remove(old_path)

            # Replace with new photo
            staffs.photo = new_photo

        staffs.save()
        return redirect('index_staff')

    return render(request, 'pages/staffs/edit.html', {'product': staffs, 'staffs': staffs})

@login_required

def staff_delete(request, id):
    staffs = get_object_or_404(Staff, id=id)
    staffs.delete()
    return redirect('index_staff')  # ← redirect to /product/index/
