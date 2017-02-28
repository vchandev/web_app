from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from posts.models import Post

class PostListView(ListView):

	model = Post


class PostDetailView(DetailView):

	model = Post
	
class PostCreate(CreateView):

	model = Post
	fields = ['title', 'slug', 'content', 'image']

class PostUpdate(UpdateView):

	model = Post
	fields = ['name']
	template_name_suffix = 'update_form'

class PostDelete(DeleteView):
   model = Post
   success_url = reverse_lazy('posts:list_posts')



	