from django import forms
from .models import Users, Data, Order, OrderDetails, Reviews, Favourites, Products, Roles, Brand, Colour, Category

#Форма пользователя
class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name','role','data']

#Форма данных аккаунта
class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['login','email','password']

#Форма заказа
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user','date','total_price','status','delivery','payment_method']

#Форма деталей заказа
class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = ['order','product','quantity']

#Форма отзывов
class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['product','rating','comment']

#Форма избранных
class FavouritesForm(forms.ModelForm):
    class Meta:
        model = Favourites
        fields = ['user','product']

#Форма товара
class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'brand', 'category', 'colour', 'photo', 'quantity']

#Форма ролей
class RolesForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = ['name']

#Форма бренда
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name','description']

#Форма цвета
class ColourForm(forms.ModelForm):
    class Meta:
        model = Colour
        fields = ['name']

#Форма категории
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description']