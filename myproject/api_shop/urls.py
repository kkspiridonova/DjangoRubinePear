from django.urls import path, include
from rest_framework import routers

from .views import (
    BrandViewSet,
    CategoryViewSet,
    ColourViewSet,
    ProductsViewSet,
    RatingViewSet,
    ReviewsViewSet,
    PayMethodViewSet,
    StatusViewSet,
    DeliveryViewSet,
    OrderViewSet,
    OrderDetailsViewSet
)

router = routers.DefaultRouter()
router.register('brands', BrandViewSet, basename='brands')
router.register('categories', CategoryViewSet, basename='categories')
router.register('colours', ColourViewSet, basename='colours')
router.register('products', ProductsViewSet, basename='products')
router.register('ratings', RatingViewSet, basename='ratings')
router.register('reviews', ReviewsViewSet, basename='reviews')
router.register('paymethods', PayMethodViewSet, basename='paymethods')
router.register('statuses', StatusViewSet, basename='statuses')
router.register('deliveries', DeliveryViewSet, basename='deliveries')
router.register('orders', OrderViewSet, basename='orders')
router.register('orderdetails', OrderDetailsViewSet, basename='orderdetails')

urlpatterns = [
    path('', include(router.urls)),
]