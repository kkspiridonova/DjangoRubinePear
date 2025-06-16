from django.db import models
from django.contrib.auth.models import User


#Роли
class Roles(models.Model):
    name = models.CharField(max_length=50, verbose_name='Роль')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

#Данные
class Data(models.Model):
    login = models.CharField(max_length=100, verbose_name='Логин')
    email=models.CharField(max_length=100,verbose_name='Почта')
    password=models.CharField(max_length=6, verbose_name='Пароль')
    
    def __str__(self):
        return f"{self.login} ({self.email})"
    
    
    class Meta:
        verbose_name = 'Данные'
        verbose_name_plural = 'Данные'

#Пользователи
class Users(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    role=models.ForeignKey(Roles, on_delete=models.PROTECT, verbose_name='Роль')
    data=models.OneToOneField(Data, on_delete=models.PROTECT, verbose_name='Личные данные')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
#Брэнд
class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название бренда')
    description = models.CharField(max_length=150, verbose_name='Описание бренда')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

#Категория
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории')
    description = models.CharField(max_length=150, verbose_name='Описание категории')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

#Цвет
class Colour(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название цвета')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

#Товар
class Products(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название товара')
    description = models.CharField(max_length=150, verbose_name='Описание товара')
    price = models.FloatField(verbose_name='Цена')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True,blank=True,verbose_name='Картинка')
    brand=models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Бренд')
    category=models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    colour=models.ForeignKey(Colour, on_delete=models.PROTECT, verbose_name='Цвет')

    def __str__(self):
        return f"{self.name} - ({self.price} рублей.)"
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

#Избранные
class Favourites(models.Model):
    user = models.ForeignKey(Users, on_delete=models.PROTECT, verbose_name='Пользователь')
    product = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='Товар')
    
    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        unique_together = ('user', 'product')

#Оценка
class Rating(models.Model):
    rating = models.IntegerField(verbose_name='Оценка')

    def __str__(self):
        return str(self.rating)
    
    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

#Отзывы
class Reviews(models.Model):
    user = models.ForeignKey(Users, on_delete=models.PROTECT, verbose_name='Пользователь')
    product = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='Товар')
    rating = models.ForeignKey(Rating, on_delete=models.PROTECT,verbose_name='Оценка')
    comment = models.CharField(max_length=150,verbose_name='Комментарий')
    date = models.DateTimeField(verbose_name='Дата',auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.comment}({self.rating})"
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

#Способы оплаты
class PayMethod(models.Model):
    name = models.CharField(max_length=50, verbose_name='Способ оплаты')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'

#Статус заказа
class Status(models.Model):
    name = models.CharField(max_length=50, verbose_name='Статус заказа')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'

#Способ доставки
class Delivery(models.Model):
    name = models.CharField(max_length=50, verbose_name='Способ доставки')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Способ доставки'
        verbose_name_plural = 'Способы доставки'

#Заказы
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    date = models.DateTimeField(verbose_name='Дата создания заказа')
    total_price = models.FloatField(verbose_name='Итоговая сумма')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Статус доставки')
    delivery = models.ForeignKey(Delivery, on_delete=models.PROTECT, verbose_name='Способ доставки')
    payment_method = models.ForeignKey(PayMethod, on_delete=models.PROTECT, verbose_name='Способ оплаты')

    def __str__(self):
        return f"{self.user.name}, {self.date}, {self.total_price}"
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

#Детали заказа
class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    product = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='Товар')
    quantity = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return f"{self.order.user}, {self.product}"
    
    class Meta:
        verbose_name = 'Детали заказа'
        verbose_name_plural = 'Детали заказов'