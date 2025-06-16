from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
from .forms import *
from basket.forms import BasketAddProductForm

def info_view(request):
    return render(request, "info.html")

#Для товаров 
class ProductsListView(ListView):
    model = Products
    template_name = 'products/products_list.html'
    context_object_name = 'products'

class ProductsDetailView(LoginRequiredMixin, DetailView):
    model = Products
    template_name = 'products/products_details.html'
    context_object_name = 'product'
    login_url = '/users/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Reviews.objects.filter(product=self.object).select_related('user', 'rating')
        context['form_basket'] = BasketAddProductForm()
        return context

class ProductsCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = Products
    form_class = ProductsForm
    template_name = 'products/products_form.html'
    success_url = reverse_lazy('products_list')
    
    def test_func(self):
        return self.request.user.is_superuser

class ProductsUpdateView(UpdateView):
    model = Products
    form_class = ProductsForm
    template_name = 'products/products_form.html'
    success_url = reverse_lazy('products_list')

class ProductsDeleteView(DeleteView):
    model = Products
    template_name = 'products/products_delete.html'
    success_url = reverse_lazy('products_list')

#Бренды
class BrandListView(ListView):
    model = Brand
    template_name = 'brand/brand_list.html'
    context_object_name = 'brand'

class BrandDetailView(DetailView):
    model = Brand
    template_name = 'brand/brand_details.html'
    context_object_name = 'brand'

class BrandUpdateView(UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'brand/brand_form.html'
    success_url = reverse_lazy('brand_list')

class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'brand/brand_delete.html'
    success_url = reverse_lazy('brand_list')

class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'brand/brand_form.html'
    success_url = reverse_lazy('brand_list')

    #Цвета
class ColourListView(ListView):
    model = Colour
    template_name = 'colour/colour_list.html'
    context_object_name = 'colour'

class ColourUpdateView(UpdateView):
    model = Colour
    form_class = ColourForm
    template_name = 'colour/colour_form.html'
    success_url = reverse_lazy('colour_list')

class ColourDeleteView(DeleteView):
    model = Colour
    template_name = 'colour/colour_delete.html'
    success_url = reverse_lazy('colour_list')

class ColourCreateView(CreateView):
    model = Colour
    form_class = ColourForm
    template_name = 'colour/colour_form.html'
    success_url = reverse_lazy('colour_list')

    #Категории
class CategoryListView(ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'category'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/category_details.html'
    context_object_name = 'category'

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories/category_delete.html'
    success_url = reverse_lazy('category_list')

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('category_list')

#Отзывы
class ReviewsListView(ListView):
    model = Reviews
    template_name = 'reviews/reviews_list.html'
    context_object_name = 'reviews'

class ReviewsCreateView(CreateView):
    model = Reviews
    form_class = ReviewsForm
    template_name = 'reviews/reviews_form.html'
    success_url = reverse_lazy('reviews_list')

#Заказы
class OrderListView(ListView):
    model = Order
    template_name = 'orders/orders_list.html'
    context_object_name = 'orders'
     
    def get_queryset(self):
        return Order.objects.select_related(
            'user', 'status', 'delivery', 'payment_method'
        ).prefetch_related('orderdetails_set__product')

class DeliveryListView(ListView):
    model = Delivery
    template_name = 'delivery/delivery_list.html'
    context_object_name = 'delivery'

class PayMethodListView(ListView):
    model = PayMethod
    template_name = 'paymethod/paymethod_list.html'
    context_object_name = 'paymethod'

class StatusListView(ListView):
    model = Status
    template_name = 'status/status_list.html'
    context_object_name = 'status'
