from django.shortcuts import render
from django.views.generic import DetailView 
from .models import Car
# Create your views here.
class CarDetailView(DetailView):
    model = Car