from django.urls import path

from my_app import views
from my_app.Views import category_views, product_views

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
    path('product/create/', product_views.product_create, name='product_create'),
    path('product/edit/<int:id>/', product_views.product_edit, name='product_edit'),
    path('product/delete/<int:id>/', product_views.product_delete, name='product_delete'),
]
