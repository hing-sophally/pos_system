import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from my_app.models import Category, Product, Position


@login_required
def index(request):
    """Display list of all users"""
    positions = Position.objects.all()
    users = User.objects.all().order_by('-date_joined')
    return render(request, "pages/users/index.html", {"users": users, "positions": positions})


@login_required
def show(request):
    """Show create user form"""
    positions = Position.objects.all()
    users = User.objects.all()
    return render(request, 'pages/users/create.html', {"users": users, "positions": positions})


@login_required
def user_create(request):
    """Create a new user"""
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        is_staff = request.POST.get('is_staff') == 'on'  # checkbox handling
        is_active = request.POST.get('is_active', 'on') == 'on'  # default to active
        is_superuser = request.POST.get('is_superuser') == 'on'  # checkbox handling

        # Validation
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            positions = Position.objects.all()
            return render(request, 'pages/users/create.html', {"positions": positions})

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            positions = Position.objects.all()
            return render(request, 'pages/users/create.html', {"positions": positions})

        try:
            # Create user
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                is_staff=is_staff,
                is_active=is_active,
                is_superuser=is_superuser
            )
            messages.success(request, 'User created successfully!')
            return redirect('index_user')
        except Exception as e:
            messages.error(request, f'Error creating user: {str(e)}')
            positions = Position.objects.all()
            return render(request, 'pages/users/create.html', {"positions": positions})

    positions = Position.objects.all()
    return render(request, 'pages/users/create.html', {"positions": positions})


@login_required
def user_edit(request, id):
    """Edit an existing user"""
    user = get_object_or_404(User, id=id)
    positions = Position.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        is_staff = request.POST.get('is_staff') == 'on'
        is_active = request.POST.get('is_active') == 'on'
        is_superuser = request.POST.get('is_superuser') == 'on'

        # Check if username is taken by another user
        if User.objects.exclude(id=user.id).filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'pages/users/edit.html', {'user': user, 'positions': positions})

        # Check if email is taken by another user
        if User.objects.exclude(id=user.id).filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'pages/users/edit.html', {'user': user, 'positions': positions})

        try:
            # Update user fields
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.is_staff = is_staff
            user.is_active = is_active
            user.is_superuser = is_superuser

            # Only update password if provided
            if password:
                user.set_password(password)

            user.save()
            messages.success(request, 'User updated successfully!')
            return redirect('index_user')
        except Exception as e:
            messages.error(request, f'Error updating user: {str(e)}')

    return render(request, 'pages/users/edit.html', {'user': user, 'positions': positions})


@login_required
def user_delete(request, id):
    """Delete a user"""
    user = get_object_or_404(User, id=id)

    # Prevent deleting the current user
    if user == request.user:
        messages.error(request, 'You cannot delete your own account.')
        return redirect('index_user')

    try:
        user.delete()
        messages.success(request, 'User deleted successfully!')
    except Exception as e:
        messages.error(request, f'Error deleting user: {str(e)}')

    return redirect('index_user')