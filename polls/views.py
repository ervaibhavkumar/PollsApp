from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader
# Create your views here.

def index(request):
    latest_ques = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_ques': latest_ques,
    }
    # output = ','.join([ q.question_text for q in latest_ques ])
    # return HttpResponse("Polls app")
    # return HttpResponse(output)
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     return Http404("Question dows not exist")

    # return HttpResponse("Yoiu are looking at question %s." % question_id)

    # return render(request, 'polls/detail.html', { 'question': question })

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', { 'question': question })

def results(request, question_id):
    response = "You are looking at results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting for question %s." % question_id)

