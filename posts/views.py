from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import PostForm
from .forms import CommentForm
from .models import Post
from .models import Comment


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class HomePageView(ListView):
    model = Comment
    template_name = 'home.html'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')

class CreateCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'home.html'
    success_url = reverse_lazy('home')

