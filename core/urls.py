from django.urls import path
from . import views

urlpatterns = [
    path('webhook', views.github_webhook, name="webhook"),
    path('' , views.homepage, name="index"),
    path('a4_letter',views.a4_letter, name="a4_letter"),
   
]
