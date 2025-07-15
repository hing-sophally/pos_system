import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from my_app.models import Major, Teacher  # Adjust app name if different
from django.contrib.auth.models import User

def index(request):
    majors = Major.objects.all()
    teachers = Teacher.objects.all()
    return render(request, "pages/teachers/index.html", {"teachers": teachers, "majors": majors})


def show(request):
    majors = Major.objects.all()
    return render(request, 'pages/teachers/create.html', {"majors": majors})


def teacher_create(request):
    majors = Major.objects.all()
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('dateOfBirth')
        salary = request.POST.get('salary')
        major_id = request.POST.get('major_id')
        photo = request.FILES.get('photo')

        teacher = Teacher.objects.create(
            firstName=first_name,
            lastName=last_name,
            gender=gender,
            dateOfBirth=date_of_birth,
            salary=salary,
            major_id=major_id if major_id else None,
            photo=photo,
            createBy=request.user if request.user.is_authenticated else None,
            updateBy=request.user if request.user.is_authenticated else None,
        )
        return redirect('index_teacher')  # Adjust to your URL name

    return render(request, 'pages/teachers/create.html', {"majors": majors})


def teacher_edit(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    majors = Major.objects.all()

    if request.method == 'POST':
        teacher.firstName = request.POST.get('firstName')
        teacher.lastName = request.POST.get('lastName')
        teacher.gender = request.POST.get('gender')
        teacher.dateOfBirth = request.POST.get('dateOfBirth')
        teacher.salary = request.POST.get('salary')
        teacher.major_id = request.POST.get('major_id')

        # Check if new photo uploaded
        if 'photo' in request.FILES:
            new_photo = request.FILES['photo']

            # Delete old photo if exists
            if teacher.photo:
                old_path = os.path.join(settings.MEDIA_ROOT, str(teacher.photo))
                if os.path.exists(old_path):
                    os.remove(old_path)

            # Replace with new photo
            teacher.photo = new_photo

        teacher.updateBy = request.user if request.user.is_authenticated else None
        teacher.save()
        return redirect('index_teacher')

    return render(request, 'pages/teachers/edit.html', {'teacher': teacher, 'majors': majors})


def teacher_delete(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    # Delete photo file if exists
    if teacher.photo:
        photo_path = os.path.join(settings.MEDIA_ROOT, str(teacher.photo))
        if os.path.exists(photo_path):
            os.remove(photo_path)

    teacher.delete()
    return redirect('index_teacher')
