import datetime

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Category(models.Model):
    """
    The category of task.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    project = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def task_due(self):
        return self.task_set.all().order_by('due')


class Task(models.Model):
    """
    Task to be completed.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start = models.DateTimeField()
    due = models.DateTimeField()
    name = models.CharField(max_length=200)
    finished = models.BooleanField(default=False)
    finished_when = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def increment(self):
        if self.priority < 20:
            self.priority += 1

    def decrement(self):
        if self.priority > 0:
            self.priority -= 1

    def subtask_priority(self):
        return self.subtask_set.all().order_by('priority')

    def clean(self):
        if hasattr(self, 'category') and hasattr(self, 'user'):
            if self.category.user != self.user:
                if self.start and self.due:
                    if self.start > self.due:
                        raise ValidationError([
                            ValidationError(_('You may only add Tasks to your own Categories/Projects.'), code='invalid'),
                            ValidationError(_('\'Due\' may not be older than \'Start\''), code='invalid'),
                        ])
                else:
                    raise ValidationError(_('You may only add Tasks to your own Categories/Projects.'), code='invalid')
        elif self.start and self.due:
            if self.start > self.due:
                raise ValidationError(_('\'Due\' may not be older than \'Start\''), code='invalid')


class SubTask(models.Model):
    """
    Smaller tasks that are part of full tasks.
    """
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    finished = models.BooleanField(default=False)
    finished_when = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def increment(self):
        if self.priority < 20:
            self.priority += 1

    def decrement(self):
        if self.priority > 0:
            self.priority -= 1


class Counter(models.Model):
    """
    attached object incrementing for tasks
    """
    subtask = models.ForeignKey(SubTask, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return str(self.count)

    def increment(self):
        if self.count < 301:
            self.count += 1

    def decrement(self):
        if self.count > 0:
            self.count -= 1


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return self.question

    def increment(self):
        if self.priority < 20:
            self.priority += 1

    def decrement(self):
        if self.priority > 0:
            self.priority -= 1


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer


class Motto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    motto = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    class Meta():
        get_latest_by = "date"

    def __str__(self):
        return self.motto
