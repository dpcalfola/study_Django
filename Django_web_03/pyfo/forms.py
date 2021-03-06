from django import forms
from pyfo.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']

        # Django form 에 model 컬럼 표시 내용 변경
        labels = {
            'subject': '제목',
            'content': '내용'
        }

        # 세밀한 html 디자인을 위해 위젯 주석처리
        #
        # # Django form 에 태그 속성 부여
        # widgets = {
        #     'subject': forms.TextInput(attrs={
        #         'class': 'form-control'
        #     }),
        #     'content': forms.Textarea(attrs={
        #         'class': 'form-control',
        #         'rows': 10
        #     })
        # }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용'
        }
