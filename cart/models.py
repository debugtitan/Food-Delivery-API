from django.db import models
from users.models import User
from store.models import FoodItem

class Cart(models.Model):
    owner = models.OneToOneField(User,on_delete=models.CASCADE,related_name='cart')
    product = models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    quantity =  models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Add a field to store the total price
    
    def update_current_item_price(self):
        self.total = self.product.item_price * self.quantity
        self.save()
        
    def __str__(self) -> str:
        return str(self.product)
    