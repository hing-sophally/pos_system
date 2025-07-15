# Add this to your views.py file in my_app

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def index_view(request):
    """
    Root URL handler that redirects users based on authentication status
    """
    if request.user.is_authenticated:
        # User is logged in, redirect to dashboard
        return redirect('home')  # 'home' is the name of your dashboard URL
    else:
        # User is not logged in, redirect to login page
        return redirect('login')


# Alternative approach using class-based view:
from django.views.generic import View
from django.utils.decorators import method_decorator


class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return redirect('login')

    def post(self, request):
        # Handle POST requests the same way
        return self.get(request)