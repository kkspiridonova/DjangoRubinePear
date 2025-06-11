from django.contrib import admin
from .models import *
@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    pass
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    pass
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(Colour)
class ColourAdmin(admin.ModelAdmin):
    pass
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    pass
@admin.register(Favourites)
class FavouritesAdmin(admin.ModelAdmin):
    pass
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass
@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    pass
@admin.register(PayMethod)
class PayMethodAdmin(admin.ModelAdmin):
    pass
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass
@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    pass
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
@admin.register(OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    pass