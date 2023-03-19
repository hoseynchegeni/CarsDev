from django.urls import path
from .views import CarDetailView, CategoryView, ProductsView, CarListView, ServiceReserve
app_name = 'products'

urlpatterns = [
    path('cars/',CarListView.as_view(),name='cars'),
    path('cars/<int:pk>/', CarDetailView.as_view(),name='CarDetail'),
    path('category/<int:id>/', CategoryView.as_view(),name='category'),
    path('products/', ProductsView.as_view(), name='products'),
    path('service/', ServiceReserve.as_view(), name='service'),
]