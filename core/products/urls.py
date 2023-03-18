from django.urls import path
from .views import CarDetailView
app_name = 'products'

urlpatterns = [
    path('cars/<int:pk>/', CarDetailView.as_view(),name='CarDetail')
]