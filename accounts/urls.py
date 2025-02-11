from django.urls import path
from .views import logout_user
from . import views

app_name = 'accounts'
urlpatterns = [
    # other URL patterns
    path('user-logout/', views.logout_user, name='logout'),
    path('user-login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
   
]
