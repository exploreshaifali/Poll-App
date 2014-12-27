#For user authentication..
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth 
from django.core.context_processors import csrf
from forms import MyRegisterationForm

from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail

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

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)	
    return render_to_response('logout.html')

def register_user(request):
    if request.method == 'POST':
        form = MyRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success/')

    # for users visiting page first time
    args = {}            
    args.update(csrf(request))

    args['form'] = MyRegisterationForm() # blank user creation form
    print(args)
    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')

class ContactWizard(SessionWizardView):
    template_name = "contact_form.html"

    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)

        return render_to_response(' done.html', {'form_data': form_data})

def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]

    send_mail(form_data[0]['subject'],
        form_data[2]['message'], form_data[1]['sender'],
        [agrawalshaifali09@gmail.com], fail_silently=False)