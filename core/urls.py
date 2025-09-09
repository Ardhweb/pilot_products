from django.urls import path
from . import views

urlpatterns = [
    path('webhook', views.github_webhook, name="webhook"),
    path('' , views.homepage, name="index"),
    path('a4_letter',views.a4_letter, name="a4_letter"),
    path('test-page',views.test_page, name="test_page"),

    path('main_editor', views.main_editor, name='main_editor'),
    path('canvas/', views.design_canvas, name='canvas'),
   
]
