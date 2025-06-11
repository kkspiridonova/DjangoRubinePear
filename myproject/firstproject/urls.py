from django.urls import path, include 
from .views import *

urlpatterns = [
    path('info', info_view, name="info_view"),
    path('', info_view),

    path('reviews',ReviewsListView.as_view(),name='reviews_list'),
    path('reviews/create',ReviewsCreateView.as_view(),name='reviews_create'),

    path('products',ProductsListView.as_view(),name='products_list'),
    path('products/<int:pk>',ProductsDetailView.as_view(),name='products_details'),
    path('products/create',ProductsCreateView.as_view(),name='products_create'),
    path('products/<int:pk>/update',ProductsUpdateView.as_view(), name='products_update'),
    path('products/<int:pk>/delete',ProductsDeleteView.as_view(), name='products_delete'),

    path('products/brand',BrandListView.as_view(),name='brand_list'),
    path('products/brand/<int:pk>',BrandDetailView.as_view(),name='brand_details'),
    path('products/brand/<int:pk>/update',BrandUpdateView.as_view(),name='brand_update'),
    path('products/brand/<int:pk>/delete',BrandDeleteView.as_view(),name='brand_delete'),
    path('products/brand/create',BrandCreateView.as_view(),name='brand_create'),


    path('products/colour',ColourListView.as_view(),name='colour_list'),
    path('products/colour/<int:pk>/update',ColourUpdateView.as_view(),name='colour_update'),
    path('products/colour/<int:pk>/delete',ColourDeleteView.as_view(),name='colour_delete'),
    path('products/colour/create',ColourCreateView.as_view(),name='colour_create'),

    path('products/category',CategoryListView.as_view(),name='category_list'),
    path('products/category/<int:pk>',CategoryDetailView.as_view(),name='category_details'),
    path('products/category/<int:pk>/update',CategoryUpdateView.as_view(),name='category_update'),
    path('products/category/<int:pk>/delete',CategoryDeleteView.as_view(),name='category_delete'),
    path('products/category/create',CategoryCreateView.as_view(),name='category_create'),
]
