from . import views
from django.urls import path


urlpatterns = [
    path('blog/',views.blog,name='blog'),
    path('blogview/',views.blogview,name='blogview'),
]