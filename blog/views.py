from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article, Category

def userStaff(request):
    if(request.user.is_authenticated):
        user_log = request.user
        # print (user_log.is_staff)
        staff = user_log.is_staff
        if staff:
            articles = Article.objects.filter(public=True)
        else: 
            articles = Article.objects.filter(public=True, private=False)
    else:
        articles = Article.objects.filter(public=True, private=False)
    
    return articles


def list(request):
    articles = userStaff(request)

    #use of paginator
    paginator = Paginator(articles, 6)
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'articles/list.html',{
        'title' : 'Artículos',
        'articles' : page_articles
    })

def category(request, category_id):
    category = get_object_or_404(Category,id=category_id)
    
    #use of paginator
    if(request.user.is_authenticated):
        user_log = request.user
        articles = Article.objects.filter(categories=category_id, public=True)
    else:
        articles = Article.objects.filter(categories=category_id, public=True, private=False)

    paginator = Paginator(articles, 6)
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'categories/category.html',{
        'category' : category,
        'articles' :page_articles
    })

def article(request, article_id):
    if(request.user.is_authenticated):
        user_log = request.user
        article = get_object_or_404(Article, id=article_id, public=True)
    else:
        article = get_object_or_404(Article, id=article_id, public=True, private=False)

    return render(request, 'articles/detail.html',{
        'article' : article
    })
