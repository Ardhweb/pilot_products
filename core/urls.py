from django.urls import path
from . import views

urlpatterns = [
    path('webhook', views.github_webhook, name="webhook"),
    path('' , views.homepage, name="index"),
    path('_blank_design',views._blank_design_generate,name="blank_design"),
    path('a4_letter',views.a4_letter, name="a4_letter"),
    path('test-page/<int:id>',views.test_page, name="test_page"),
    path('view-page-pdf',views.view_page_pdf, name="view_page_pdf"),

]
