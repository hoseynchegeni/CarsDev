from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from django.views import View
from .models import Car, ProductCategory, Product, Services
from django.db.models import Q

# Create your views here.
class CarListView(ListView):
    model = Car
    queryset = Car.objects.all()
    context_object_name = "cars"


class CarDetailView(DetailView):
    model = Car


class CategoryView(View):
    def get(self, request, id):
        obj = Product.objects.filter(category_id=id)
        return render(request, "products/category.html", {"obj": obj})
    
class SearchResultView(ListView):
    model = ProductCategory
    def get_queryset(self):
        query = self.request.GET.get('q')
        return ProductCategory.objects.filter(
            Q(name__contains = query)
        )


class ProductsView(ListView):
    model = Product
    queryset = Product.objects.filter(status=True)
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product


class ServiceReserve(CreateView):
    model = Services
    fields = [
        "type",
        "phone",
        "car_name",
        "reserve_for",
    ]
    success_url = "/home/"
