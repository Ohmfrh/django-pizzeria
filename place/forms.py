from django import forms

from place.models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['customer', 'pizzas']
