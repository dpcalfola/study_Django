from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from rest_framework.views import APIView
from .models import Question


# Create your views here.


def index(request):
    """
    pyfo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}

    return render(request, 'pyfo/question_list.html', context)


def detail(request, question_id):
    """
    pyfo 내용 출력
    """
    # 객체를 그냥 읽어오는 방법
    # question = Question.objects.get(id=question_id)

    # DB 에서 불러올 객체가 없을 경우 404에러를 띄우는 방법
    question = get_object_or_404(Question, pk=question_id)

    context = {'question': question}
    return render(request, 'pyfo/question_detail.html', context)


def answer_create(request, question_id):
    """
    pyfo 답변 등록
    """

    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pyfo:detail', question_id=question.id)
