# Updated major views with proper user tracking
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from my_app.models import Major


@login_required
def index(request):
    majors = Major.objects.all()
    return render(request, "pages/majors/index.html", {'majors': majors})


@login_required
def major_create(request):
    if request.method == 'POST':
        subject_name = request.POST.get('SubjectName')
        try:
            with transaction.atomic():
                Major.objects.create(
                    SubjectName=subject_name,
                    CreateBy=request.user,  # Set the user who created this major
                    CreateAt=timezone.now()
                )
        except Exception as e:
            print("Create Error:", e)
            return redirect('error_page')
        return redirect('index_major')
    return render(request, 'pages/majors/create.html')


@login_required
def major_edit(request, id):
    major = get_object_or_404(Major, id=id)
    if request.method == 'POST':
        try:
            subject_name = request.POST.get('SubjectName')
            if Major.objects.exclude(id=major.id).filter(SubjectName=subject_name).exists():
                error_message = f"The major '{subject_name}' already exists."
                return render(request, 'pages/majors/edit.html', {'major': major, 'error_message': error_message})

            with transaction.atomic():
                major.SubjectName = subject_name
                major.UpdateBy = request.user  # Set the user who updated this major
                major.UpdateAt = timezone.now()
                major.save()
        except Exception as e:
            print("Edit Error:", e)
            return render(request, 'pages/error.html', {'error_message': str(e)})
        return redirect('index_major')
    return render(request, 'pages/majors/edit.html', {'major': major})


@login_required
def major_delete(request, id):
    major = get_object_or_404(Major, id=id)
    try:
        with transaction.atomic():
            major.delete()
    except Exception as e:
        print("Delete Error:", e)
        return redirect('error_page')
    return redirect('index_major')