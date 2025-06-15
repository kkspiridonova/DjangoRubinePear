from django import forms
from firstproject.models import Order

class BasketAddProductForm(forms.Form):
   count = forms.IntegerField(min_value=1,initial=1,label='Количество', widget=forms.NumberInput(attrs={'class':'form-control'}))
   reload=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivery', 'payment_method']
        labels = {
            'delivery': 'Способ доставки',
            'payment_method': 'Способ оплаты',
        }
        widgets = {
            'delivery': forms.Select(attrs={'class': 'form-select'}),
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
        }