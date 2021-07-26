from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Netflix, Comment
from .forms import netflixForm, CommentForm

# Create your views here.

def home(request):
    article = Netflix.objects.all()
    articleList = Netflix.objects.all()
    paginator = Paginator(articleList, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request,'home.html',{'article' : article, 'posts' : posts})

def detail(request, article_id):
    article_detail = get_object_or_404(Netflix, pk = article_id)
    comments = Comment.objects.filter(netflix_id=article_id, comment_id__isnull=True)

    re_comments = []
    for comment in comments:
        re_comments += list(Comment.objects.filter(comment_id=comment.id))
    
    form = CommentForm()
    return render(request, 'detail.html' ,{'article' : article_detail, 'comments' : comments, 're_comments' : re_comments, 'form':form})

def new(request):
    if request.method == 'POST': #폼 다채우고 저장버튼 눌렀을 때
        form = netflixForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('detail', post.id)
        return redirect('home')
    else:  #글을 쓰기위해 들어갔을 때
        form = netflixForm()
        return render(request,'new.html', {'form':form})


def edit(request, article_id):
    post = get_object_or_404(Netflix, pk = article_id)
    if request.method == 'GET':  #수정하려고 들어갔을 때
        form = netflixForm(instance = post)
        return render(request, 'edit.html', {'form' : form})
    else:   #수정 끝나고 수정 버튼을 눌렀을 때
        form = netflixForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('/netflixapp/detail/' + str(article_id))
        return redirect('home')

def delete(request, article_id):
    article_delete =  Netflix.objects.get(id = article_id)
    article_delete.delete()
    return redirect('home')

def search(request):
    blogs = Netflix.objects.all().order_by('-id')

    find = request.POST.get('find', "")

    if find:
        blogs = blogs.filter(title__icontains=find)
        return render(request, 'search.html', {'blogs': blogs, 'find':find})
    else:
        return render(request, 'search.html')

def create_comment(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.netflix_id = Netflix.objects.get(pk=article_id)
            comment.save()
    return redirect('detail', article_id)

def create_re_comment(request, article_id, comment_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.netflix_id = Netflix.objects.get(pk=article_id)
            comment.comment_id = Comment.objects.get(pk=comment_id)
            comment.save()
    return redirect('detail', article_id)

def delete_comment(request, comment_id, article_id):
    mycom = Comment.objects.get(id=comment_id)
    mycom.delete()

    return redirect('detail', article_id)
