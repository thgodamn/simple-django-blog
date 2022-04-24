from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Article #, Comment
from django.urls import reverse
#from django.http import HttpResponse

# Create your views here.

def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})
    #return render(request, 'articles/list.html')
    #return HttpResponse('Привет мир')

def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена')

    latest_coments_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'articles/detail.html', {'article': a, 'latest_coments_list': latest_coments_list})


def add_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена')
    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)) )