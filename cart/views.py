from django.shortcuts import render, get_object_or_404
from .cart import Cart
from django.contrib import messages
from store.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_summary(req):
    cart = Cart(req)
    cart_products = cart.get_prods()
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(req, "cart_summary.html", {'cart_products': cart_products, 'quantities': quantities, "totals": totals})

def cart_add(req):
    cart = Cart(req)
    if req.method == 'POST' and req.POST.get('action') == 'post':
        product_id = int(req.POST.get('product_id'))
        product_qty = int(req.POST.get('product_qty'))
        
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        
        cart_quantity = cart.__len__()
        
        #response_data = {'Product Name': product.name} 
        response_data = {'qty': cart_quantity}  
        messages.success(req, "Product add to cart")
        return JsonResponse(response_data)

    
def cart_delete(req):
    cart = Cart(req)
    if req.method == 'POST' and req.POST.get('action') == 'post':
        try:
            product_id = int(req.POST.get('product_id'))
            cart.delete(product=product_id)
            response = JsonResponse({'product': product_id})
            messages.success(req, "Item has been deleted!!!")
            return response
        except KeyError:
            return JsonResponse({'error': 'Product not found'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
    
def cart_update(req):
    cart = Cart(req)
    if req.method == 'POST' and req.POST.get('action') == 'post':
        product_id = int(req.POST.get('product_id'))
        product_qty = int(req.POST.get('product_qty'))
        
        cart.update(product = product_id, quantity = product_qty)
        
        response = JsonResponse({'qty': product_qty})
        messages.success(req, "Cart has been updated !!!")
        return response