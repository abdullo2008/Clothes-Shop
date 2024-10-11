from django.urls import path

from .views import *

urlpatterns = [
    # API`s urls
    path('api/v1/', CreateListProduct.as_view(), name='api_product'),
    path('api/v1/<int:pk>/', UpDelRetProduct.as_view(), name='api_product'),
    path('api/v1/users/', CreateListUser.as_view(), name='api_user'),
    path('api/v1/users/<int:pk>/', UpDelRetUser.as_view(), name='api_user'),
    path('api/v1/category/', CreateListCategory.as_view(), name='api_category'),
    path('api/v1/category/<int:pk>/', UpDelRetCategory.as_view(), name='api_category')
    # Site`s urls

]
