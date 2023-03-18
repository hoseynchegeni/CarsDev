from django.urls import path
from .views import CarDetailView, CategoryView
app_name = 'products'

urlpatterns = [
    path('cars/<int:pk>/', CarDetailView.as_view(),name='CarDetail'),
    path('category/<int:id>/', CategoryView.as_view(),name='category'),
]