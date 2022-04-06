from django.urls import path

from . import views

app_name = 'pyfo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create_02, name='answer_create'),
]