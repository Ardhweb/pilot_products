from django.urls import path
from .views import logout_user
from . import views

app_name = 'accounts'
urlpatterns = [
    # other URL patterns
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.register, name='register'),
   
]
