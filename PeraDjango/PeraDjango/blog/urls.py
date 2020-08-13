from django.contrib import admin
from django.urls import path, include
from .views import blog, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(PostListView.as_view()), name='blog-list'),
    path('<int:pk>/', login_required(PostDetailView.as_view()), name='blog-detail'),
    path('update/<int:pk>/', login_required(PostUpdateView.as_view()), name='blog-update'),
    path('delete/<int:pk>/', login_required(PostDeleteView.as_view()), name='blog-delete'),
    path('create', login_required(PostCreateView.as_view()), name='blog-create'),
]
