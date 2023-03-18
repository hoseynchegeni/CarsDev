from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView
from .models import Post
from products.models import Car, ProductCategory
# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(status = True, is_news = False)
        context['news'] = Post.objects.filter(status = True, is_news = True)
        context['cars'] = Car.objects.all()
        context['categories'] = ProductCategory.objects.all()
        return context
    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['author','title','content','status','is_news','published_date']
    success_url = '/home/'
