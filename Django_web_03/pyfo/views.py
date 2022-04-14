from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import QuestionForm, AnswerForm
from .models import Question, Answer


# Create your views here.


def index(request):
    """
    pyfo 목록 출력
    """

    # input parameter
    page = request.GET.get('page', 1)

    # search
    question_list = Question.objects.order_by('-create_date')

    # paging
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
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
    pyfo 답변 등록, Answer 모델 이용
    """
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.save()
            return redirect('pyfo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {
        'question': question,
        'form': form,
    }
    return render(request, 'pyfo/question_detail.html', context)


# 질문 생성 (QuestionForm)
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pyfo:index')
    else:
        form = QuestionForm()

    context = {'form': form}
    return render(request, 'pyfo/question_form.html', context)


# 질문 삭제
# def question_delete(request):


#
# 사용하지 않음 (참고용 코드)
def answer_create_old_01(request, question_id):
    """
    pyfo 답변 등록
    """

    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pyfo:detail', question_id=question.id)


# 사용하지 않음 (참고용 코드)
def answer_create_old_02(request, question_id):
    """
    pyfo 답변등록, Answer 모델 이용
    :param request: Question object
    :param question_id: question.id
    :return: redirect(pyfo:detail, question_id=question.id)
    """
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('pyfo:detail', question_id=question.id)
