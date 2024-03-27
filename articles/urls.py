from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.article_list),
]

#date = models.DateTimeField(auto_now_add=True)
    #date = models.DateTimeField(auto_now_add=True)
    #date = models.DateTimeField(auto_now_add=True)
    #date = models.DateTimeField(auto_now_add=True)
    #date = models.DateTimeField(auto_now_add=True)