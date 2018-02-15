from django import forms

from place.models import Order, ReceiptItem


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name']


class AddPizzaForm(forms.models.ModelForm):

    class Meta:
        model = ReceiptItem
        fields = ['quantity', 'pizza']
