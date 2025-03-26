from django.urls import path
from . import views
from .views import PDFView
from .utils import dynamic_spinner_script
urlpatterns = [
    path('coverit/my-letters',views.indexing_cover_l, name="cover_listing"),
    path('coverit/', views.create_cover, name="create_cover"),
    path('coverit/cover-view/<int:id>/<str:title>/', views.cover_th, name='cover_view'),
    path('coverit/generate-pdf/<int:id>/', PDFView.as_view(), name='generate_pdf'),
    path('genai-google/', views.generate_text_view, name='generate_gemini'),
    #utility
    path("spinner-script.js", dynamic_spinner_script, name="spinner_script"),
]
