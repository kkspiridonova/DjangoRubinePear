from rest_framework import serializers
from firstproject.models import *


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'description']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']


class ColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colour
        fields = ['name']


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'photo', 'brand', 'category', 'colour']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['rating']


class ReviewsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    product = ProductsSerializer(read_only=True)
    rating = RatingSerializer(read_only=True)
    date = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)

    class Meta:
        model = Reviews
        fields = ['user', 'product', 'rating', 'comment', 'date']


class PayMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayMethod
        fields = ['name']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['name']


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['name']


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    status = StatusSerializer(read_only=True)
    delivery = DeliverySerializer(read_only=True)
    payment_method = PayMethodSerializer(read_only=True)
    date = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)

    class Meta:
        model = Order
        fields = ['user', 'date', 'total_price', 'status', 'delivery', 'payment_method']


class OrderDetailsSerializer(serializers.ModelSerializer):
    order = serializers.StringRelatedField()
    product = ProductsSerializer(read_only=True)

    class Meta:
        model = OrderDetails
        fields = ['order', 'product', 'quantity']
