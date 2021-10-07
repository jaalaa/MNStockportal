from article.form import ArticleForm
from django.core import paginator
from django.shortcuts import render
from article.models import Article
from django.core.paginator import Paginator
from django.contrib import messages


def index(request):
    objs = Article.objects.all()
    # 一覧に表示する記事の件数
    paginator = Paginator(objs, 3)
    page_number = request.GET.get('page')
    context = {
        'page_obj' : paginator.get_page(page_number),
        'page_number' : page_number
    }
    return render(request, 'article/articles.html', context)    

def article(request,pk):
    obj = Article.objects.get(pk=pk)
    context = {
        'article' : obj
    }
    return render(request, 'article/article.html', context)

def new(request):
    context = {}
    # print('----',request.POST, request.FILES)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        article = form.save(commit=False)
        article.save()
        messages.success(request,'saved')

    return render(request, 'article/new.html', context)
