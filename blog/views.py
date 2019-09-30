from django.shortcuts import render
from django.http import  HttpResponse
from blog.models import Article
from django.core.paginator import Paginator

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = 'title:%sbrief-content:%s;content:%s;article_id"%s;publish_date:%s' \
                 % (title,brief_content,content,article_id,publish_date)
    return HttpResponse(return_str)

#blog主页面
def get_index_page(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    article_list = Article.objects.all()
    top5_article_list = Article.objects.order_by('-publish_date')[:5]
    all_article = Paginator(article_list, 5)
    article_page = all_article.page(page)
    all_page = all_article.num_pages
    if 1-article_page.has_next():
        next_page = page
        previous_page = page - 1
    elif 1-article_page.has_previous():
        previous_page = page
        next_page = page + 1
    else:
        next_page = page + 1
        previous_page = page - 1
    return render(request,'blog/index.html',
                  {
                      'top5_article_list':top5_article_list,
                      'curr_article_list':article_page,
                      'all_page':range(1,all_page+1),
                      'previous_page':previous_page,
                      'next_page':next_page
                  }
                 )


#文章详情页面
def get_detail_page(request,article_id):
    all_article = Article.objects.all()
    previous_index = None
    next_index = None
    for index,article in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article)-1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.article_id == article_id:
            curr_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break
    section_list = curr_article.content.split('\n')
    return render(request,'blog/detail.html',
                  {
                      'title':curr_article.title,
                      'section_list':section_list,
                      'previous_article':previous_article,
                      'next_article':next_article
                  }
                  )