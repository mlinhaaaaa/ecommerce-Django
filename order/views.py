from django.shortcuts import render
from cart.cart import Cart

# Create your views here.
def payment_success(req):
    cart = Cart(req)
    cart_products = cart.get_prods()
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(req, "order/payment_success.html", {'cart_products': cart_products, 'quantities': quantities, "totals": totals})

def checkout(req):
    cart = Cart(req)
    cart_products = cart.get_prods()
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(req, "order/checkout.html", {'cart_products': cart_products, 'quantities': quantities, "totals": totals})