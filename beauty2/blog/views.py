from.models import * 
from django.shortcuts import render 
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .forms import ArticleSearchForm
from math import ceil

def article(request, title):
    article = get_object_or_404(Article, title=title.replace('-', ' '))

    if 'article_' + str(article.id) not in request.session:
        request.session['article_' + str(article.id)] = True
        article.view += 1
        article.save()

    related_articles = []
    if article.category:
        category_count = Article.objects.filter(category=article.category).exclude(id=article.id).count()
        if category_count > 0:
            related_articles = Article.objects.filter(Q(category=article.category) & ~Q(id=article.id) | ~Q(category=article.category)).distinct()[:2]
        else:
            related_articles = Article.objects.exclude(category=None).exclude(id=article.id)[:2]
    else:
        related_articles = Article.objects.exclude(category=None).exclude(id=article.id)[:2]
        
        

    context = {
        'article': article,
        'related_articles': related_articles,
    }
    return render(request, 'blog/article.html', context)


# صحفه مقالات   


def category_articles(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    articles = Article.objects.filter(category=category)
    context = {'category': category , 'articles':articles}
    return render(request, 'blog/articles.html', context)





def articles(request):
    category = Category.objects.all()
    form = ArticleSearchForm(request.GET or None)
    articles = Article.objects.all()
    article_list = Article.objects.all()
    per_page = 6
    paginator = Paginator(article_list, per_page)
    total_pages = ceil(article_list.count() / per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'form': form, 'category': category, 'total_pages': total_pages , 'articles':articles}
    return render(request, 'blog/articles.html', context)