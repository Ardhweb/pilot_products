from django.urls import path
from . import views

urlpatterns = [
    path('webhook', views.github_webhook, name="webhook"),
    path('about' , views.about_us, name="about"),
    path('privacy-polices' , views.privacy_policy, name="privacy-polices"),
    path('' , views.homepage, name="index"),
   
]
