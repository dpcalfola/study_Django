from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Question
from django.template import loader


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)


def index_old(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ' <br>'.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def page(request, page_num):
    pages = 'polls/page_' + str(page_num) + '.html'
    print(pages)
    return render(request, pages)

