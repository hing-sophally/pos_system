from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from my_app.serializers import RegisterSerializer, LoginSerializer


# Basic views
def home(request):
    return render(request, "index.html")


def content(request):
    return render(request, "pages/content.html")


def error_page(request):
    return render(request, 'pages/error.html')


def register_login(request):
    return render(request, "register_login.html")


# Authentication views (Form-based)
def login_view(request):
    if request.user.is_authenticated:
        return redirect('major_list')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Login successful!')
                next_url = request.GET.get('next', 'major_list')
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid credentials.')
        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials.')

    return render(request, 'register_login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('major_list')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')

        # Basic validation
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            messages.success(request, 'Registration successful! Please login.')
            return redirect('login')

    return render(request, 'register_login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


# API Views for AJAX/API requests
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User registered successfully.",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"message": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

            user = authenticate(username=user.username, password=password)
            if user:
                login(request, user)
                return Response({
                    "message": "Login successful!",
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                    }
                }, status=status.HTTP_200_OK)
            return Response({"message": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


