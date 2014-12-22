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

def auth_view(request):
    username = request.POST.get('username', '')	
    # empty string specify if username value does not exist in POST dictonary yet
    # then return an empty string
    password = request.POST.get('password', '')

    # main check is here
    user = auth.authenticate(username=username, password=password)

    if user is not None:
    	# set status of user to loggedin as user is authenticated
    	auth.login(request, user)
    	return HttpResponseRedirect('/accounts/loggedin')
    else:
    	return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('loggedin.html', {'full_name' : request.user.username})   

