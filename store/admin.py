from django.contrib import admin
from .models import  Categories,FoodItem
from django.utils.html import format_html

admin.site.register(Categories)

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'category', 'display_image', 'item_price', 'created_at')
    
    

    def display_image(self, obj):
        if obj.item_image:
            return format_html(f'<img src="{obj.item_image.url}" alt="{obj.item_name}" style="max-height: 100px; max-width: 100px;" />')
        return "No Image"
    
    display_image.allow_tags = True
    display_image.short_description = 'Food Image'

admin.site.register(FoodItem, FoodItemAdmin)