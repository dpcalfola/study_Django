8000/admin 페이지에서 모델을 관리하기 위해서는 
app 내부의 apps.py 에 설정을 추가해야함

코드 >
(polls.admin.py)

from django.contrib import admin

from .models import Question

admin.site.register(Question)

-> .models 의 Question 클래스를 불러온다

-> admin site 가 관리하도록 register