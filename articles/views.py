from django.shortcuts import render
from articles.models import Article
# Create your views here.
def article_index(request):
	artiles_list = Article.objects.order_by('pub_date')
	context = {'artiles_list': artiles_list}
	return render(request, 'articles/index.html', context)