from django.urls import path

from my_app import views
from my_app.Views import category_views, product_views, position_views, staff_views

urlpatterns = [
    path("",views.home,name="home"),
    path("content",views.content,name="content"),

# Category Route

    path("category/index",category_views.index,name="index"),
    path('category/create/', category_views.category_create, name='category_create'),
    path('category/edit/<int:id>/', category_views.category_edit, name='category_edit'),
    path('category/delete/<int:id>/', category_views.category_delete, name='category_delete'),


# Product Route

    path("product/index",product_views.index,name="index"),
    path("product/show",product_views.show , name='product_show'),
    path('product/create/', product_views.product_create, name='product_create'),
    path('product/edit/<int:id>/', product_views.product_edit, name='product_edit'),
    path('product/delete/<int:id>/', product_views.product_delete, name='product_delete'),


# Positions Route

    path("position/index",position_views.index,name="index"),
    path('position/create/', position_views.position_create, name='position_create'),
    path('position/edit/<int:id>/', position_views.position_edit, name='position_edit'),
    path('position/delete/<int:id>/', position_views.position_delete, name='position_delete'),


# Staff Route

    path("staff/index",staff_views.index,name="index"),
    path("staff/show",staff_views.show , name='staff_show'),
    path('staff/create/', staff_views.staff_create, name='staff_create'),
    path('staff/edit/<int:id>/', staff_views.staff_edit, name='staff_edit'),
    path('staff/delete/<int:id>/', staff_views.staff_delete, name='staff_delete'),

]