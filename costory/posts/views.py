from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
# from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse 
from .models import Post
from .forms import PostForm
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-dt_created']
    paginate_by = 6
    page_kwarg = 'page'
# def post_list(request):
#     posts = Post.objects.all()
#     paginator = Paginator(posts, 6)
#     curr_page_number = request.GET.get('page')
#     if curr_page_number is None:
#         curr_page_number = 1
#     page = paginator.page(curr_page_number)
#     return render(request, 'posts/post_list.html', {'page': page} )

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'
# def post_detail(request, post_id):
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         raise Http404()
#     context = {'post': post}
#     return render(request, 'posts/post_detail.html', context=context)

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.id})

# class PostCreateView(View):
#     def get(self, request):
#         post_form = PostForm()
#         return render(request, 'posts/post_form.html', {'form' : post_form})
        
#     def post(self, request):
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#             new_post = post_form.save()
#             return redirect('post-detail', post_id=new_post.id) 

# def post_create(request):
#     if request.method == 'POST':
#         # title = request.POST['title']
#         # content = request.POST['content']
#         # new_post = Post(
#         #     title = title,
#         #     content = content,
#         # )
#         # new_post.save()
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#             new_post = post_form.save()
#             return redirect('post-detail', post_id=new_post.id)       
#     else:
#         post_form = PostForm()
#     return render(request, 'posts/post_form.html', {'form' : post_form})

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    pk_url_kwarg = 'post_id'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.id})
# def post_update(request, post_id):
#     post = Post.objects.get(id=post_id)
#     if request.method == 'POST':
#         post_form = PostForm(request.POST, instance=post)
#         if post_form.is_valid():
#             post_form.save()
#             return redirect('post-detail', post_id=post.id)
#     else:
#         post_form = PostForm(instance=post)
#     return render(request, 'posts/post_form.html', {'form': post_form})

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('post-list')
# def post_delete(request, post_id):
#     post = Post.objects.get(id=post_id)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post-list')
#     else:
#         return render(request, 'posts/post_confirm_delete.html', {'post': post})

def index(request):
    return redirect('post-list')