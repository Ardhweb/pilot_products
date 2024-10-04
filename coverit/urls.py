from django.urls import path
from . import views
from .views import PDFView
urlpatterns = [
    path('', views.index, name="index"),
    path('coverit/your-cover/listing/',views.indexing_cover_l, name="cover_listing"),
    path('coverit/made-cover', views.create_cover, name="create_cover"),
    path('coverit/cover-view/<int:id>/<str:title>/', views.cover_th, name='cover_view'),
    path('coverit/generate-pdf/<int:id>/', PDFView.as_view(), name='generate_pdf'),
]
