from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy


#def first_view(request):
    #return render(request, 'first.html')

#def second_view(request):
    #return render(request, 'second.html')


def main_page(request):
    return render(request, 'main_page.html')

def catalog_page(request):
    return render(request, 'catalog.html')

def conatcts_page(request):
    return render(request, 'contacts.html')

def cart(request):
    return render(request, 'cart.html')

def how_to_find(request):
    return render(request, 'how_to_find.html')

def categories(request):
    return render(request, 'categories.html')

def cabinet(request):
    return render(request, 'cab.html')

def adminpanel(request):
    return render(request, 'admin_panel.html')

def category_detail(request, id):
    category_name = f"Категория номер {id}" 
    data = {
        'category_name': category_name,
        'category_id': id,
    }
    return render(request, 'category_detail.html', data)


#гитары
class GuitarListView(ListView):
    model = Guitar
    template_name = 'guitar/guitar_list.html'
    context_object_name = 'guitars'

class GuitarDetailView(DetailView):
    model = Guitar
    template_name = 'guitar/guitar_detail.html'
    context_object_name = 'guitar'

class GuitarCreateView(CreateView):
    model = Guitar
    template_name = 'guitar/guitar_form.html'
    fields = ['name', 'description', 'price', 'photo', 'in_shop_quantity', 'guitar_form', 'category', 'is_exists']
    success_url = reverse_lazy('guitar_list_view')

class GuitarUpdateView(UpdateView):
    model = Guitar
    template_name = 'guitar/guitar_form.html'
    fields = ['name', 'description', 'price', 'photo', 'in_shop_quantity', 'guitar_form', 'category', 'is_exists']
    success_url = reverse_lazy('guitar_list_view')

class GuitarDeleteView(DeleteView):
    model = Guitar
    template_name = 'guitar/guitar_confirm_delete.html'
    success_url = reverse_lazy('guitar_list_view')

#категории
class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category/category_form.html'
    fields = ['name', 'photo', 'description']
    success_url = reverse_lazy('category_list_view')

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category/category_form.html'
    fields = ['name', 'photo', 'description']
    success_url = reverse_lazy('category_list_view')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/category_confirm_delete.html'
    success_url = reverse_lazy('category_list_view')

#формы
class GuitarFormListView(ListView):
    model = GuitarForm
    template_name = 'guitarform/guitarform_list.html'
    context_object_name = 'guitarforms'

class GuitarFormDetailView(DetailView):
    model = GuitarForm
    template_name = 'guitarform/guitarform_detail.html'
    context_object_name = 'guitarform'

class GuitarFormCreateView(CreateView):
    model = GuitarForm
    template_name = 'guitarform/guitarform_form.html'
    fields = ['name']
    success_url = reverse_lazy('guitarform_list_view')

class GuitarFormUpdateView(UpdateView):
    model = GuitarForm
    template_name = 'guitarform/guitarform_form.html'
    fields = ['name']
    success_url = reverse_lazy('guitarform_list_view')

class GuitarFormDeleteView(DeleteView):
    model = GuitarForm
    template_name = 'guitarform/guitarform_confirm_delete.html'
    success_url = reverse_lazy('guitarform_list_view')

#корзина
class CartListView(ListView):
    model = Cart
    template_name = 'cart/cart_list.html'
    context_object_name = 'carts'

class CartDetailView( DetailView):
    model = Cart
    template_name = 'cart/cart_detail.html'
    context_object_name = 'cart'

class CartCreateView(CreateView):
    model = Cart
    template_name = 'cart/cart_form.html'
    fields = ['user']
    success_url = reverse_lazy('cart_list_view')

class CartUpdateView(UpdateView):
    model = Cart
    template_name = 'cart/cart_form.html'
    fields = ['user']
    success_url = reverse_lazy('cart_list_view')

class CartDeleteView(DeleteView):
    model = Cart
    template_name = 'cart/cart_confirm_delete.html'
    success_url = reverse_lazy('cart_list_view')

#заказ
class OrderListView(ListView):
    model = Order
    template_name = 'order/order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/order_detail.html'
    context_object_name = 'order'

class OrderCreateView(CreateView):
    model = Order
    template_name = 'order/order_form.html'
    fields = ['user', 'status', 'address', 'comment', 'total_price']
    success_url = reverse_lazy('order_list_view')

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order/order_form.html'
    fields = ['user', 'status', 'address', 'comment', 'total_price']
    success_url = reverse_lazy('order_list_view')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order/order_confirm_delete.html'
    success_url = reverse_lazy('order_list_view')

#статус
class StatusListView(ListView):
    model = OrderStatus
    template_name = 'status/status_list.html'
    context_object_name = 'statuses'

class StatusDetailView(DetailView):
    model = OrderStatus
    template_name = 'status/status_detail.html'
    context_object_name = 'status'

class StatusCreateView(CreateView):
    model = OrderStatus
    template_name = 'status/status_form.html'
    fields = ['name']
    success_url = reverse_lazy('status_list_view')

class StatusUpdateView(UpdateView):
    model = OrderStatus
    template_name = 'status/status_form.html'
    fields = ['name']
    success_url = reverse_lazy('status_list_view')

class StatusDeleteView(DeleteView):
    model = OrderStatus
    template_name = 'status/status_confirm_delete.html'
    success_url = reverse_lazy('status_list_view')

#позиция в корзине
class CartItemListView(ListView):
    model = CartItem
    template_name = 'cartitem/cartitem_list.html'
    context_object_name = 'cartitems'

class CartItemDetailView(DetailView):
    model = CartItem
    template_name = 'cartitem/cartitem_detail.html'
    context_object_name = 'cartitem'

class CartItemCreateView(CreateView):
    model = CartItem
    template_name = 'cartitem/cartitem_form.html'
    fields = ['quantity', 'cart', 'guitar']
    success_url = reverse_lazy('cartitem_list_view')

class CartItemUpdateView(UpdateView):
    model = CartItem
    template_name = 'cartitem/cartitem_form.html'
    fields = ['quantity', 'cart', 'guitar']
    success_url = reverse_lazy('cartitem_list_view')

class CartItemDeleteView(DeleteView):
    model = CartItem
    template_name = 'cartitem/cartitem_confirm_delete.html'
    success_url = reverse_lazy('cartitem_list_view')


#позиция в заказе
class OrderItemListView(ListView):
    model = OrderItem
    template_name = 'orderitem/orderitem_list.html'
    context_object_name = 'orderitems'

class OrderItemDetailView(DetailView):
    model = OrderItem
    template_name = 'orderitem/orderitem_detail.html'
    context_object_name = 'orderitem'

class OrderItemCreateView(CreateView):
    model = OrderItem
    template_name = 'orderitem/orderitem_form.html'
    fields = ['quantity', 'price', 'guitar', 'order']
    success_url = reverse_lazy('orderitem_list_view')

class OrderItemUpdateView(UpdateView):
    model = OrderItem
    template_name = 'orderitem/orderitem_form.html'
    fields = ['quantity', 'price', 'guitar', 'order']
    success_url = reverse_lazy('orderitem_list_view')

class OrderItemDeleteView(DeleteView):
    model = OrderItem
    template_name = 'orderitem/orderitem_confirm_delete.html'
    success_url = reverse_lazy('orderitem_list_view')


