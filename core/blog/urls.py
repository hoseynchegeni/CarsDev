from django.urls import path
from .views import Index,PostDetailView, PostCreateView

app_name = 'blog'

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path("post/<int:pk>/", PostDetailView.as_view(), name="PostDetail"),
    path('post/create/',PostCreateView.as_view(), name = 'create'),
]