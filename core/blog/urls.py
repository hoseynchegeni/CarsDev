from django.urls import path
from .views import Index,PostDetailView

app_name = 'blog'

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path("post/<int:pk>/", PostDetailView.as_view(), name="PostDetail"),
]