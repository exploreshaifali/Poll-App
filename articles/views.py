from django.shortcuts import render
from articles.models import Article
from django.views import generic

from django.http import HttpResponse
# Create your views here.

class IndexView(generic.ListView):
	template_name = 'articles/index.html'
	context_object_name = 'articles_list'

	def get_queryset(self):
		"""Retutn last 9 published articles"""
		return Article.objects.order_by('pub_date')[:9]

def article_all(request):
	'''return list of all articles'''
	language = 'en-us' #will be stored in cookies
	session_language = 'en-us' #will be stored in sessions

	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']

	articles_list = Article.objects.all()
	context = {'articles_list' : articles_list, 'language' : language}
	return render(request, 'articles/all.html', context)

def article(request, article_id):
	'''return article whose id is given in function argument'''
	article = Article.objects.get(id = article_id)
	context = {'article': article}
	return render(request, 'articles/article.html', context)

def language(request, language='en-us'):
	response = HttpResponse("setting language to %s" % language)
	response.set_cookie('lang', language)
	return response


# def article_index(request):
# 	'''return the list of articles present in databse'''
# 	articles_list = Article.objects.order_by('pub_date')
# 	context = {'articles_list': articles_list}
# 	return render(request, 'articles/index.html', context)

