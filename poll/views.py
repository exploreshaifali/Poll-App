from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from poll.models import Question

def index(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.question_text for p in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at poll %s." % question_id)

def results(request, question_id):
    return HttpResponse("You're looking at the results of poll %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on poll %s." % question_id)    