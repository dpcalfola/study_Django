from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Question


# Create your views here.

class Index(APIView):

    def get(self, request):
        """
        pyfo 목록 출력
        """
        question_list = Question.objects.order_by('-create_date')
        context = {'question_list': question_list}

        return render(request, 'pyfo/index.html', context)

    def post(self, request):
        return HttpResponse("Hello!! This is pyfo!!")


class Detail(APIView):

    def get(self, request, question_id):
        """
        pyfo 내용 출력
        """
        question = Question.objects.get(id=question_id)
        context = {'question': question}
        return render(request, 'pyfo/question_detail.html', context)
