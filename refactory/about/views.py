from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader
# Create your views here.
def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
