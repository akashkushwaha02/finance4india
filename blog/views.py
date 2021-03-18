from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Blog
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from .models import Blog,BlogCategory
from .forms import BlogForm,UpdateBlogForm
from django.urls import reverse_lazy,reverse
# Create your views here.

# def home(request):        
#     return render(request,'blog/home.html')

def LikeView(request,pk):
    post = get_object_or_404(Blog,id=request.POST.get('blog_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('details',args=[str(pk)]))


def CategoryView(request,cat):
    category_posts = Blog.objects.filter(category=cat.replace('-',' '))
    return render(request,'blog/category.html',{'cat':cat.title().replace('-',' ') ,'category_posts':category_posts})

class HomeView(ListView):
    model = Blog
    template_name = 'blog/home.html'
    ordering = ['-created_at']


    def get_context_data(self,*args,**kwargs):
        cat_menu = BlogCategory.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context['cat_menu'] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Blog
    template_name = 'blog/details.html'

    def get_context_data(self,*args,**kwargs):
        cat_menu = BlogCategory.objects.all()
        context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        context['cat_menu'] = cat_menu
        return context


class CreatBlogView(CreateView):
    model = Blog 
    form_class = BlogForm
    template_name = 'blog/addPost.html'
    #fields = ('title','title_tag','author','description')

class AddCategoryView(CreateView):
    model = BlogCategory 
    template_name = 'blog/addCategory.html'
    fields = '__all__'


class UpdateBlogView(UpdateView):
    model = Blog
    form_class = UpdateBlogForm    
    template_name ='blog/update_blog.html'
    #fields = ('title','title_tag','description')

class DeleteBlogView(DeleteView):
    model = Blog
    template_name ='blog/delete_blog.html'
    success_url = reverse_lazy('home')