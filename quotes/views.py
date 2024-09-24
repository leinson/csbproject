from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.http import Http404
from .models import Question, Choice
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

#TODO
#CRYPTOGRAPHIC FAILURE 
#   save password without hashing
    #"create user" functionality
    #
#INJECTION (SQL)
    #in the create user functionality
    #add quote


#VULNERABLE&OUTDATED COMPONENTS 
#   add an old library/extension?

#SECURITY MISCONFIGURATION
#   link to admin page & password displayed
#DONE
#CSRF 
#   in html&settings.py
#BROCEN ACCESS CONTROL
#   easy admin password & access to admin functionality


@login_required
@csrf_exempt #remove this 
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'quotes/index.html', context)

#@login_required <- broken access control, add this to fix
@csrf_exempt
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quotes/detail.html', {'question': question})

#@login_required <- broken access control, add this to fix
@csrf_exempt
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'quotes/results.html', {'question': question})
    
#@login_required <- broken access control, add this to fix
@csrf_exempt
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'quotes/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
       
        return HttpResponseRedirect(reverse('quotes:results', args=(question.id,)))

