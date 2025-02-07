from django.urls import path
from . import views

app_name = 'timeline'
urlpatterns = [
   
    path('create-daily/', views.create_parent, name='create_daily'),
    path('your-item/', views.parent_list, name='list_daily'),
    path('add-item/<int:id>', views.add_item, name='item_add'),
]
