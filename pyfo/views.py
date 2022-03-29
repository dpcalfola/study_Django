from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.

class Index(APIView):

    def get(self, request):
        return HttpResponse("Hello!! This is pyfo!!")

    def post(self, request):
        return HttpResponse("Hello!! This is pyfo!!")
