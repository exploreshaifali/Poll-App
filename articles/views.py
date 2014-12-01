from django.shortcuts import render
from articles.models import Article
# Create your views here.
def article_index(request):
	articles_list = Article.objects.order_by('pub_date')
	context = {'articles_list': articles_list}
	return render(request, 'articles/index.html', context)