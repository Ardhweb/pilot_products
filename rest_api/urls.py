from django.urls import path
from . import views
app_name="rest_api"
urlpatterns = [
    path('cover-chat-query', views.draft_for_letter, name="cover_chat_query")
]
