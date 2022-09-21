from django.contrib import admin
from app.models import Customer, OrderPlaced,Product, Cart, OrderPlaced
from django.contrib.auth.admin import UserAdmin




# Register your models here.





@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user' , 'name' , 'locality' , 'city' , 'zipcode' , 'state']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title' , 'selling_price' , 'discounted_price', 'description' ,'brand', 'category', 'product_images']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user' , 'product' , 'quantity']


@admin.register(OrderPlaced)
class OrederPlacedAdmin(admin.ModelAdmin):
    list_display = ['user' , 'customer' , 'product' , 'quantity' , 'order_date' , 'status']



