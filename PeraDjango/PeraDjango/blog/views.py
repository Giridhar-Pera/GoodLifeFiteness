from abc import ABC

from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


# Create your views here.
@login_required(login_url='/login')
def blog(request):
    posts = Blog.objects.all()
    return render(request, 'blog_latest.html', {'posts': posts})


class PostListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog_latest.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'post_detail.html'


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView, ABC):
    model = Blog
    template_name = 'post_delete.html'
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        else:
            return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'description']
    template_name = 'post_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) and redirect('/blog')


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, ABC):
    model = Blog
    fields = ['title', 'description']
    template_name = 'post_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) and redirect('/blog')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        else:
            return False
