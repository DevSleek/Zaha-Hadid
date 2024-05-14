from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/create.html'
    fields = ('title', 'description', 'photo', 'teaching_category',)
    success_url = reverse_lazy('home')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/update.html'
    fields = ('title', 'description', 'photo', 'teaching_category',)
    success_url = reverse_lazy('home')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('home')
