from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from firstproject.models import Products, Order, OrderDetails, Status
from .basket import Basket
from .forms import BasketAddProductForm, OrderForm
from django.http import HttpResponseForbidden



def basket_detail(request):
    if request.user.is_superuser:
        return HttpResponseForbidden("Администраторам доступ в корзину запрещен.")
    basket = Basket(request)
    return render(request, 'basket/detail.html', {'basket': basket})


@require_POST
def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Products, pk=product_id)
    basket.remove(product)
    return redirect('basket_detail')


def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket_detail')


@require_POST
@login_required
def basket_add(request, product_id):
    if request.user.is_superuser:
        return HttpResponseForbidden("Администраторам доступ в корзину запрещен.")

    basket = Basket(request)
    product = get_object_or_404(Products, pk=product_id)
    form = BasketAddProductForm(request.POST)

    if form.is_valid():
        count = form.cleaned_data['count']
        update = form.cleaned_data['reload']
        current_quantity = product.quantity
        existing_count = basket.basket.get(str(product.id), {}).get('count', 0)
        new_count = count if update else existing_count + count

        if new_count > current_quantity:
            # ⚠ Если товара не хватает, не добавляем и просто отрисовываем страницу
            warning = f"Нельзя добавить {count} шт. товара — на складе только {current_quantity}."
            return render(request, 'basket/detail.html', {
                'basket': basket,
                'warning': warning
            })

        # Если всё нормально — добавляем товар и редиректим
        basket.add(product=product, count=count, update_count=update)
        return redirect('basket_detail')

    # Если форма невалидна
    return redirect('basket_detail')


@login_required
def basket_buy(request):
    if request.user.is_superuser:
        return HttpResponseForbidden("Администраторам доступ в корзину запрещен.")
    basket = Basket(request)

    if len(basket) <= 0:
        return redirect('list_product.filter') 

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.date = timezone.now()
            order.total_price = basket.get_total_price()
            order.status = Status.objects.get_or_create(name='Ожидает обработки')[0] 
            order.save()

            for item in basket:
                OrderDetails.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['count']
                )

            basket.clear()
            return redirect('info_view') 
    else:
        form = OrderForm()

    return render(request, 'order/order_form.html', {
        'form_order': form,
        'basket': basket
    })


@login_required
def open_order(request):
    """Возможно, устаревшая в контексте новой логики"""
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.date = timezone.now()
            order.status = Status.objects.get_or_create(name='Ожидает обработки')[0]
            order.total_price = 0  # или пересчитать вручную
            order.save()
            return redirect('info_view')
    else:
        form = OrderForm()

    return render(request, 'order/order_form.html', {
        'form_order': form,
        'basket': Basket(request)
    })
