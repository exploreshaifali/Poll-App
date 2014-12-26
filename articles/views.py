from django.shortcuts import render
from articles.models import Article
from django.views import generic

from django.http import HttpResponse

from forms import ArticleForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

import django.shortcuts
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

	#getting value from cookies
	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']

	#getting value from sessions
	if 'lang' in request.session:
		session_language = request.session['lang']

	articles_list = Article.objects.all()
	context = {'articles_list' : articles_list,
				'language' : language, 'session_language' : session_language}
	return render(request, 'articles/all.html', context)

def article(request, article_id):
	'''return article whose id is given in function argument'''
	article = Article.objects.get(id = article_id)
	context = {'article': article}
	return render(request, 'articles/article.html', context)

def language(request, language='en-us'):
	response = HttpResponse("setting language to %s" % language)
	response.set_cookie('lang', language)
	request.session['lang'] = language

	return response

def create(request):
    if request.method == 'POST':
    	form = ArticleForm(request.POST, request.FILES)
    	if form.is_valid():
    		form.save()
    		return HttpResponseRedirect('/articles/all')

    else:
    	form = ArticleForm()

    args = {}    	
    args.update(csrf(request))

    args['form'] = form
    # print(args)

    return render_to_response('create_article.html', args)
    # return render(request, 'create_article.html', args)

def like_article(request, article_id):
	a = Article.objects.get(id=article_id)
	a.likes += 1
	a.save()

	return HttpResponseRedirect('/articles/get/%s' % article_id)

def search_titles(request):
	'''Return the article whose title matches to seatch_text'''
	if request.method == 'POST':
		search_text = request.POST['search_text']
	else:
		search_text = ''

	articles = Article.objects.filter(title__constrains=search_text)
	context = {'articles': articles}
	return render('ajax_search.html', context)
	