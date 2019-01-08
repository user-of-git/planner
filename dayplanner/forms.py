from django import forms
from .models import Category, Task, SubTask, Question, Answer, Motto


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['user', 'name', 'project']


class TaskForm(forms.ModelForm):
    start = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'])
    due = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'])

    class Meta:
        model = Task
        fields = ['user', 'category', 'start', 'due', 'name', 'priority']
    
    def clean(self):
        super().clean()
        start = self.cleaned_data.get("start")
        due = self.cleaned_data.get("due")
        if start and due:
            if start > due:
                self.add_error('due', ' may not be older than \'Start\'')
        category = self.cleaned_data.get("category")
        if category.user != self.cleaned_data.get("user"):
            self.add_error('category', ' You may only add Tasks to your own Categories/Projects.')



class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['task', 'name', 'priority']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['user', 'question', 'priority']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['question', 'answer']


class MottoForm(forms.ModelForm):
    class Meta:
        model = Motto
        fields = ['user', 'motto']


class DateForm(forms.Form):
    date = forms.DateField(label='Enter Date (YYYY-MM-DD)')
