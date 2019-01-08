from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from . import views


urlpatterns = [
    # home and daily tasks
    path('', views.HomeView.as_view(), name='home'),
    path('user', views.user, name='user'),
    path('introduction', views.introduction, name='introduction'),
    # archive
    path('archive', views.archive, name='archive'),
    path('archive/<int:year>/<int:month>/<int:day>', views.archive_get, name='archive_get'),
    # others
    path('copy_yesterday', views.copy_yesterday, name='copy_yesterday'),
    path('copy_task/<int:task_id>', views.copy_task, name='copy_task'),
    path('previous_<int:days>_days', views.previous_days, name='previous_days'),
    path('library', views.library, name='library'),
    path('projects', views.projects, name='projects'),
    path('deadlines', views.deadlines, name='deadlines'),
    # add
    path('add_category', views.add_category, name='add_category'),
    path('add_task', views.add_task, name='add_task'),
    path('add_subtask/<int:task_id>', views.add_subtask, name='add_subtask'),
    path('add_question', views.add_question, name='add_question'),
    path('add_answer/<int:question_id>', views.add_answer, name='add_answer'),
    path('add_motto', views.add_motto, name='add_motto'),
    # edit
    path('edit_category/', views.edit_category, name='edit_category'),
    path('edit_task/<int:task_id>', views.edit_task, name='edit_task'),
    path('edit_subtask/<int:subtask_id>', views.edit_subtask, name='edit_subtask'),
    path('add_counter/<int:subtask_id>', views.add_counter, name='add_counter'),
    path('edit_question/<int:question_id>', views.edit_question, name='edit_question'),
    path('edit_answer/<int:answer_id>', views.edit_answer, name='edit_answer'),
    path('edit_motto/', views.edit_motto, name='edit_motto'),
    # delete
    path('delete', views.delete, name='delete'),
    path('delete_category', views.delete_category, name='delete_category'),
    # finish
    path('task_finished/<int:task_id>', views.task_finished, name='task_finished'),
    path('task_not_finished/<int:task_id>', views.task_not_finished, name='task_not_finished'),
    path('subtask_finished/<int:subtask_id>', views.subtask_finished, name='subtask_finished'),
    path('subtask_not_finished/<int:subtask_id>', views.subtask_not_finished, name='subtask_not_finished'),
    # counter
    path('increment_counter/<int:counter_id>', views.increment_counter, name='increment_counter'),
    path('decrement_counter/<int:counter_id>', views.decrement_counter, name='decrement_counter'),
    # priority
    path('task_priority_increment/<int:task_id>', views.task_priority_increment, name='task_priority_increment'),
    path('task_priority_decrement/<int:task_id>', views.task_priority_decrement, name='task_priority_decrement'),
    path('subtask_priority_increment/<int:subtask_id>', views.subtask_priority_increment, name='subtask_priority_increment'),
    path('subtask_priority_decrement/<int:subtask_id>', views.subtask_priority_decrement, name='subtask_priority_decrement'),
    path('question_priority_increment/<int:question_id>', views.question_priority_increment, name='question_priority_increment'),
    path('question_priority_decrement/<int:question_id>', views.question_priority_decrement, name='question_priority_decrement'),
]
