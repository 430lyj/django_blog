from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Blog, Comment
from .forms import BlogForm, CommentForm
from django.core.paginator import Paginator
import math
from account.models import CustomUser
from django.db.models import F

# Create your views here.
def home (request):
    blogs = Blog.objects.order_by('-pub_date')
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    paginated_blogs = paginator.get_page(page)
    n = math.ceil(len(blogs) / 3 )
    return render(request, 'home.html', {'blogs':paginated_blogs, 'range':range(1, n+1), 'ten':range(1, 11), 'n': len(blogs)})

def detail (request, id):
    blog = Blog.objects.get(id = id)
    comments = Comment.objects.filter(blog = blog)
    new_comment = Comment()
    if request.method == 'POST':
        new_comment.body = request.POST['body']
        new_comment.blog = blog
        if request.user.is_authenticated:
            new_comment.user = request.user
        new_comment.save()
    return render(request, 'detail.html', {'blog':blog, 'comments':comments})

def new (request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.pub_date = timezone.now()
    new_blog.image = request.FILES['image']
    new_blog.body = request.POST['body']
    new_blog.save()
    return redirect('blog:detail', new_blog.id)

def update(request, id):
    blog = Blog.objects.get(id = id)
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.save()
        return redirect('blog:detail', blog.id)
    return render(request, 'update.html', {'blog':blog})

def delete(request, id):
    blog = Blog.objects.get(id = id)
    blog.delete()
    return redirect('home')

def new_with_django_form (request):
    form = BlogForm()
    if request.user.is_authenticated:
        return render(request, 'new_with_django_form.html', {'form':form})
    return redirect('account:login')

def create_with_django_form(request):
    form = BlogForm(request.POST, request.FILES) # form 데이터를 처리하기 위해서 request.POST와 request.FILES가 필요함을 의미합니다.
    if form.is_valid(): # 유효성 검사 
        new_blog = form.save(commit=False) # 임시 저장 나머지 필드(칼럼)를 채우기 위함
        new_blog.writer = request.user
        new_blog.user = request.user
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('blog:detail', new_blog.id)
    return redirect('home')

def searchpage(request):
    user = request.user
    blogs = Blog.objects.filter(writer = user)
    paginator = Paginator(blogs, 3) # blogs를 3개씩 쪼갠다
    page = request.GET.get('page') # 해당 정보가 오지 않아도 넘어간다
    paginated_blogs = paginator.get_page(page)
    n = len(blogs)
    return render(request, 'search.html', {'blogs' : blogs, 'n':n})

def search_univ(request):
    univUser = request.user
    blogs = Blog.objects.select_related('user').filter(user__university = univUser.university)
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    paginated_blogs = paginator.get_page(page)
    n = math.ceil(len(blogs) / 3 )
    return render(request, 'searchUniv.html', {'blogs':paginated_blogs, 'range':range(1, n+1), 'ten':range(1, 11), 'n': len(blogs)})

def commentDelete(request, id):
    comment = Comment.objects.get(id=id)
    blog_id = comment.blog.id
    comment.delete()
    return redirect('blog:detail', blog_id)