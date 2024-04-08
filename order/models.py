from django.db import models
from django.contrib.auth.models import User
from store.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    shipping_address = models.CharField(max_length = 10000)
    amout_paid = models.DecimalField(max_digits = 10, decimal_places=2)
    date_order = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Order - {str(self.id)}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    
    def __str__(self):
        return f'Order Item - {str(self.id)}'
    
