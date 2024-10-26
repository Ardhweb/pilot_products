from django.urls import path
from . import views

urlpatterns = [
    path('password-generator' , views.password_gen, name="password-generator"),
   
]
