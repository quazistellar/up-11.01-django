from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Guitar, GuitarForm, Category, Cart, Order, OrderStatus, CartItem, OrderItem
from django.urls import reverse_lazy

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm
from cartapp.forms import BasketAddProductForm


def main_page(request):
    return render(request, 'main_page.html')

def catalog_page(request):
    guitars = Guitar.objects.all() 
    return render(request, 'catalog.html', {'guitars': guitars})

def conatcts_page(request):
    return render(request, 'contacts.html')

def cart(request):
    return render(request, 'cart.html')

def how_to_find(request):
    return render(request, 'how_to_find.html')

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def cabinet(request):
    user = request.user
    orders = Order.objects.filter(user=user).exclude(status__name="Завершен").order_by('-create_date')  
    context = {
        'user': user,
        'orders': orders,
    }
    return render(request, 'cab.html', context)


@login_required
def adminpanel(request):
    return render(request, 'admin_panel.html')


def category_detail(request, id):
    category = get_object_or_404(Category, pk=id)
    guitars = Guitar.objects.filter(category=category, is_exists=True)
    data = {
        'category': category,
        'guitars': guitars,
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
    fields = ['address', 'total_price', 'user', 'status', 'first_name', 'last_name', 'middle_name', 'end_date']
    success_url = reverse_lazy('order_list_view')

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order/order_form.html'
    fields = ['address', 'total_price', 'user', 'status', 'first_name', 'last_name', 'middle_name', 'end_date']
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


# подробная информация 
class GuitarOnClickDetailView(DetailView):
    model = Guitar
    template_name = 'guitar_detail_view.html'
    context_object_name = 'guitar'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm()
        return context

# для авторизации регистрации и выхода

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('catalog')
    else:
        form = LoginForm()
        return render(request, 'auth/login.html', context={'form': form})


def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)  
        if form.is_valid():
            user = form.save() 
            login(request, user) 
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
            return redirect('catalog')
        else:
            return render(request, 'auth/registration.html', context={'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'auth/registration.html', context={'form': form})
    

def logout_user(request):
    logout(request)
    return redirect('catalog')