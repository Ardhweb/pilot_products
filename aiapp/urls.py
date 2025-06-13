from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('aiapp',TemplateView.as_view(template_name="test.html"),name="aihome"),

]