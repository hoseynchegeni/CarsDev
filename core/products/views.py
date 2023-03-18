from django.shortcuts import render
from django.views.generic import DetailView
from django.views import View 
from .models import Car, ProductCategory, Product
# Create your views here.
class CarDetailView(DetailView):
    model = Car

class CategoryView(View):
    def get(self, request, id):
        obj = Product.objects.filter(category_id = id)
        return render(request, 'products/category.html', {'obj':obj})