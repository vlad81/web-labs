from . import tasks
from django.http import HttpResponse
from django.shortcuts import render


def send_email_view(request):
    task_id = tasks.send_email.apply_async(queue='send_email', args=(['sinomis639@64ge.com'],))
    return HttpResponse(f'Sending of email. Task id {task_id}')


def long_task_view(request):
    task_id = tasks.long_work.apply_async(queue='long_work', args=(5,))
    return HttpResponse(f'Task id: {task_id}')

