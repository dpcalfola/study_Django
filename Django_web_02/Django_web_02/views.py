from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):

    def get(self, request):
        print('get 호출')
        return render(request, "Django_web_02/main.html")

    def post(self, request):
        print('post 호출')

        return render(request, "Django_web_02/main.html")
