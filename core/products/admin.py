from django.contrib import admin
from .models import Car, Product, ProductCategory, Services

# Register your models here.
admin.site.register(Car)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Services)
