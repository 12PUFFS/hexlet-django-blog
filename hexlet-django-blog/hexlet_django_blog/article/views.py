# hexlet_django_blog/article/views.py
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render (
        request,
        'articles/index.html',
        context={
            'name': 'acticle',
        },
    )
