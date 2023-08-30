from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    created = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = 'Item Category'
        verbose_name_plural = 'Item Categories'
        
    def __str__(self) -> str:
        return str(self.name)
        

class FoodItem(models.Model):
    category =  models.OneToOneField(Categories,on_delete=models.CASCADE,related_name='food')
    item_name = models.CharField(max_length=50,primary_key=True)
    item_image = models.FileField(upload_to='items/',null=True,blank=True)
    item_price = models.DecimalField(decimal_places=2,max_digits=7)
    created_at = models.DateField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return str(self.item_name)