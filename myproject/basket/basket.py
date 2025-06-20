from django.conf import settings
from firstproject.models import Products

class Basket:

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def __iter__(self):
        product_ids = self.basket.keys()
        product_list = Products.objects.filter(pk__in=product_ids)

        basket = self.basket.copy()
        for product in product_list:
            basket[str(product.pk)]['product'] = product

        for item in basket.values():
            item['total_price'] = float(item['price']) * int(item['count'])
            yield item

    def __len__(self):
        return sum(int(item['count']) for item in self.basket.values())

    def save(self):
        self.session[settings.BASKET_SESSION_ID] = self.basket
        self.session.modified = True

    def add(self, product, count=1, update_count=False):
        product_id = str(product.id)
        current_quantity = product.quantity 

        existing_count = self.basket.get(product_id, {}).get('count', 0)

        if update_count:
            if count > current_quantity:
                return 
            self.basket[product_id] = {
                'count': count,
                'price': str(product.price)
            }
        else:
            new_count = existing_count + count
            if new_count > current_quantity:
                return  
            self.basket[product_id] = {
                'count': new_count,
                'price': str(product.price)
            }

        self.save()


    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def get_total_price(self):
        return sum(
            float(item['price']) * int(item['count'])
            for item in self.basket.values()
        )

    def clear(self):
        if settings.BASKET_SESSION_ID in self.session:
            del self.session[settings.BASKET_SESSION_ID]
            self.session.modified = True
