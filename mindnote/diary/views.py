from django.core import paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Page
from .forms import PageForm

# Create your views here.
class PageListView(ListView):
    model = Page
    template_name = 'diary/page_list.html'
    context_object_name = 'pages'
    ordering = ['-dt_created']
    paginate_by = 8
    page_kwarg = 'page'
# def page_list(request):
#     pages = Page.objects.all()
#     paginator = Paginator(pages, 8)
#     curr_page_num = request.GET.get('page')
#     if curr_page_num is None:
#         curr_page_num = 1
#     pagelt = paginator.page(curr_page_num)
#     return render(request, 'diary/page_list.html', {'pagelt': pagelt} )

class PageDetailView(DetailView):
    model = Page
    template_name = 'diary/page_detail.html'
    pk_url_kwarg = 'page_id'
    context_object_name = 'page'
# def page_detail(request, page_id):
#     context = dict()
#     page = Page.objects.get(id=page_id)
#     context['page'] = page
#     return render(request, 'diary/page_detail.html', context=context )

def info(request):
    return render(request, 'diary/info.html')

class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    template_name = 'diary/page_form.html'

    def get_success_url(self):
        return reverse('page-detail', kwargs={'page_id': self.object.id})

# def page_create(request):
#     if request.method == 'POST':
#         # title = request.POST['title']
#         # content = request.POST['content']
#         # feeling = request.POST['feeling']
#         # score = request.POST['score']
#         # dt_created = request.POST['dt_created']
#         # new_page = Page(
#         #     title = title,
#         #     content = content,
#         #     feeling = feeling,
#         #     score = score,
#         #     dt_created = dt_created,
#         # )
#         # new_page.save()
#         new_form = PageForm(request.POST)
#         if new_form.is_valid():
#             new_page = new_form.save()
#             return redirect('page-detail', page_id=new_page.id)
#     else:
#         new_form = PageForm()
#     return render(request, 'diary/page_form.html', {'new_page' : new_form})

class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'diary/page_form.html'
    pk_url_kwarg = 'page_id'

    def get_success_url(self):
        return reverse('page-detail', kwargs={'page_id': self.object.id})
# def page_update(request, page_id):
#     page = Page.objects.get(id=page_id)
#     if request.method == 'POST':
#         new_form = PageForm(request.POST, instance=page)
#         if new_form.is_valid():
#            new_form.save()
#            return redirect('page-detail', page_id=page.id)
#     else:
#         new_form = PageForm(instance=page)
#     return render(request, 'diary/page_form.html', {'new_page' : new_form })

class PageDeleteView(DeleteView):
    model = Page
    template_name = 'diary/page_confirm_delete.html'
    pk_url_kwarg = 'page_id'
    context_object_name = 'page'

    def get_success_url(self):
        return reverse('page-list')
# def page_delete(request, page_id):
#     page = Page.objects.get(id=page_id)
#     if request.method == 'POST':
#         page.delete()
#         return redirect('page-list')
#     else:
#         return render(request, 'diary/page_confirm_delete.html',{'page': page})

def index(request):
    return render(request, 'diary/index.html')
    