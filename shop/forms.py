from django import forms

from .models import *

class GuitarForm(forms.ModelForm):
    class Meta:
        model = Guitar
        fields = ['name', 'description', 'price', 'photo', 'color', 'photo', 'in_shop_quantity', 'is_exists', 'category', 'guitar_form']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'photo', 'description']

class GuitarFormForm(forms.ModelForm):
    class Meta:
        model = GuitarForm
        fields = ['name']


class Order(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'total_price', 'user', 'status']


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user']

class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = OrderStatus
        fields = ['name']

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity', 'cart', 'guitar']

class OrderitemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity', 'price', 'guitar', 'order']