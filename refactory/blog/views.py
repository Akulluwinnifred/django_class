from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def blog(request):
    template = loader.get_template('blog.html')
    return HttpResponse(template.render())


def blogview(request):
    template = loader.get_template('blogview.html')
    return HttpResponse(template.render())