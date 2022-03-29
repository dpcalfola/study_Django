from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('<int:question_id>/', views.Detail.as_view())
]
