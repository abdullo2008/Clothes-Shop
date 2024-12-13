from django.urls import path

from .views import *

urlpatterns = [
    # API`s urls
    path('api/v1/', CreateListProduct.as_view(), name='api_product'),
    path('api/v1/<int:pk>/', UpDelRetProduct.as_view(), name='api_product'),
    path('api/v1/category/', CreateListCategory.as_view(), name='api_category'),
    path('api/v1/category/<int:pk>/', UpDelRetCategory.as_view(), name='api_category'),
    # Site`s urls
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('product/<int:id>/', single, name='single'),
    path('category/<int:id>/', single_category, name='category'),
    path('search/', search, name='search'),
    # Category urls
    path('category/list/', CategoryList, name='category_list'),
    path('category/add/', CategoryAdd.as_view(), name='category_add'),
    path('category/update/<int:pk>/', CategoryUpdate.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDelete.as_view(), name='category_delete'),
    # Product urls
    path('product/add/', ProductAdd.as_view(), name='product_add'),
    path('product/update/<int:pk>/', ProductUpdate.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDelete.as_view(), name='product_delete'),
    # Authentification
    path('login/', LoginPage, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutPage, name='logout'),
    path('users', Users, name='users'),
    path('user', user, name='user'),
]
