#For user authentication..
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth 
from django.core.context_processors import csrf


def main_page(request):
    return render_to_response('index.html')

def home(request):
	return HttpResponse("Hello Welcome to poll's app.")

def login(request):
	'''if request is vallid not fake move to the login template
	wich will redirect to auth_view()
	'''
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

