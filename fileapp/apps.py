from django.apps import AppConfig


class FileappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fileapp'

    from django.shortcuts import render
from django.http import HttpResponse

def registration(request):
    # Your registration logic here
    return HttpResponse('Registration page')

