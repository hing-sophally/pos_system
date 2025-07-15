from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from my_app import views
from my_app.Views import category_views, product_views, position_views, staff_views, major_views, teacher_views, \
    user_views
from my_app.views import RegisterAPIView, LoginAPIView

urlpatterns = [
    # ... your existing url patterns ...

    # Example:
    path("dashboard", views.home, name="home"),
    path("content", views.content, name="content"),
    path('error/', views.error_page, name='error_page'),
    path("", views.register_login, name="login"),
    path('api/auth/register', RegisterAPIView.as_view(), name='api_register'),
    path('api/auth/login', LoginAPIView.as_view(), name='api_login'),

    # Category Routes
    path("category/index", category_views.index, name="index_category"),
    path('category/create/', category_views.category_create, name='category_create'),
    path('category/edit/<int:id>/', category_views.category_edit, name='category_edit'),
    path('category/delete/<int:id>/', category_views.category_delete, name='category_delete'),

    # Product Routes
    path("product/index", product_views.index, name="index_product"),
    path("product/show", product_views.show, name='product_show'),
    path('product/create/', product_views.product_create, name='product_create'),
    path('product/edit/<int:id>/', product_views.product_edit, name='product_edit'),
    path('product/delete/<int:id>/', product_views.product_delete, name='product_delete'),

    # Position Routes
    path("position/index", position_views.index, name="index_position"),
    path('position/create/', position_views.position_create, name='position_create'),
    path('position/edit/<int:id>/', position_views.position_edit, name='position_edit'),
    path('position/delete/<int:id>/', position_views.position_delete, name='position_delete'),

    # Staff Routes
    path("staff/index", staff_views.index, name="index_staff"),
    path("staff/show", staff_views.show, name='staff_show'),
    path('staff/create/', staff_views.staff_create, name='staff_create'),
    path('staff/edit/<int:id>/', staff_views.staff_edit, name='staff_edit'),
    path('staff/delete/<int:id>/', staff_views.staff_delete, name='staff_delete'),

    # Major Routes
    path('major/index/', major_views.index, name="index_major"),
    path('major/create/', major_views.major_create, name='major_create'),
    path('major/edit/<int:id>/', major_views.major_edit, name='major_edit'),
    path('major/delete/<int:id>/', major_views.major_delete, name='major_delete'),

    # Teacher Routes
    path("teacher/index", teacher_views.index, name="index_teacher"),
    path("teacher/show", teacher_views.show, name="teacher_show"),
    path("teacher/create/", teacher_views.teacher_create, name="teacher_create"),
    path("teacher/edit/<int:id>/", teacher_views.teacher_edit, name="teacher_edit"),
    path("teacher/delete/<int:id>/", teacher_views.teacher_delete, name="teacher_delete"),


# User Route
    path("user/index", user_views.index, name="index_user"),
    path("user/show", user_views.show, name="user_show"),
    path("user/create/", user_views.user_create, name="user_create"),
    path("user/edit/<int:id>/", user_views.user_edit, name="user_edit"),
    path("user/delete/<int:id>/", user_views.user_delete, name="user_delete"),
]

# Add this at the end of the file:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
