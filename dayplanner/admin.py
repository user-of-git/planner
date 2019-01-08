from django.contrib import admin
from .models import Category, Task, SubTask, Counter, Question, Answer, Motto

# Register your models here.
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(SubTask)
admin.site.register(Counter)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Motto)
