from django.urls import path
from . import views
from .views import PDFView
urlpatterns = [
    path('', views.index, name="index"),
    path('made-cover', views.create_cover, name="create_cover"),
    path('cover-view/<int:id>/<str:title>/', views.cover_th, name='cover_view'),
    path('generate-pdf/<int:id>/', PDFView.as_view(), name='generate_pdf'),
]
