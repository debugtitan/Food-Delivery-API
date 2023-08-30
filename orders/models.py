import uuid
from django.db import models
from users.models import User
from cart.models import Cart
from phonenumber_field.modelfields import PhoneNumberField

class Orders(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled')
    ]
    order_id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='order')
    items = models.ManyToManyField(Cart)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=90,default="")
    contact = PhoneNumberField(region='NG', max_length=15,default="")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = self.generate_order_id()
        super().save(*args, **kwargs)
    
    def generate_order_id(self):
        prefix = "FlavorFleet"
        unique_id = uuid.uuid4().hex[:10]
        return f"{prefix}-{unique_id}"
    
   
    
    class Meta:
        verbose_name = 'Order Processed'
        verbose_name_plural = 'Orders Processed'
        
    def __str__(self):
        return f"Order #{self.order_id}"
