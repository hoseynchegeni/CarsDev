from django.urls import path
from .views import (
    CarDetailView,
    CategoryView,
    ProductsView,
    CarListView,
    ServiceReserve,
    ProductDetailView,
    SearchResultView,
)

app_name = "products"

urlpatterns = [
    path("cars/", CarListView.as_view(), name="cars"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="CarDetail"),
    path("category/<int:id>/", CategoryView.as_view(), name="category"),
    path('search/',SearchResultView.as_view(), name = 'search'),
    path("products/", ProductsView.as_view(), name="products"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="ProductsDetail"),
    path("service/", ServiceReserve.as_view(), name="service"),
]
