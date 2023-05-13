from.models import * 
from django.shortcuts import render 
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .forms import ArticleSearchForm


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
def articles(request):
    category = Category.objects.all()
    form = ArticleSearchForm(request.GET or None)
    search_query = request.GET.get('search')
    articles = Article.objects.all()
    
    
    if request.method == 'POST' and search_query:
        article_list = Article.objects.filter(title__icontains=search_query)
    elif search_query:
        article_list = Article.objects.filter(title__icontains=search_query)
    else:
        article_list = Article.objects.all()

    paginator = Paginator(article_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'form': form , 'articles':articles , 'category' : category}
    return render(request, 'blog/articles.html', context)