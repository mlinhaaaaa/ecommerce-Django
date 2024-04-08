from . cart import Cart

def cart(req):
    return {'cart': Cart(req)}