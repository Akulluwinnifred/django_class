from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def about(request):
    return HttpResponse("Hello world,this is all about the refactory class for cohort 2024")
