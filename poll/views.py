from django.shortcuts import render, get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from poll.models import Question, Choice

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    #latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now())
    context = {'latest_question_list': latest_question_list}
    return render(request, 'poll/index.html', context)

@login_required
def detail(request, question_id):
    #return HttpResponse("You're looking at poll %s." % question_id)
    question = get_object_or_404(Question, pk=question_id, pub_date__lte=timezone.now())
    return render(request, 'poll/detail.html', {'question': question})  

@login_required
def results(request, question_id):
    #return HttpResponse("You're looking at the results of poll %s." % question_id)
    question = get_object_or_404(Question, pk=question_id, pub_date__lte=timezone.now())    
    return render(request, 'poll/results.html', {'question': question,})

@login_required
def vote(request, question_id):
    #return HttpResponse("You're voting on poll %s." % question_id)    
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'poll/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll:results', args=(p.id,)))
