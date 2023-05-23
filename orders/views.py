from django.shortcuts import render
from .models import Orders, OrderItem
from cart.cart import Cart
from .forms import OrderCreatedForm
from .tasks import order_created

def create_orders(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreatedForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, quantity=item['quantity'], price=item['price'],
                                         product=item['product'])
            cart.clear()
            order_created.delay(order.id)
            return render(request, 'orders/order/created.html', {'order': order})
    else:

        form = OrderCreatedForm()
    return render(request, 'orders/order/create.html', {'form': form})

# Create your views here.
