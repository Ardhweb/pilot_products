from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('made-cover', views.create_cover, name="create_cover"),
]
