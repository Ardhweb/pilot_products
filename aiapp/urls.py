from django.urls import path
from django.views.generic import TemplateView
from aiapp import views

urlpatterns = [
    path('aiapp',TemplateView.as_view(template_name="test.html"),name="aihome"),
    path('analyzer/upload-file/',views.analyzer_upload, name="analyzer_upload"),

]