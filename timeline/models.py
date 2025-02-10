from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User
# Create your models here.
class Timeline(BaseModel):
    title = models.CharField(max_length=50, blank=True, null=True)
    mark_delete = models.BooleanField(default=False)
    

class TimelineNode(BaseModel):
    time_line =  models.ForeignKey(Timeline, on_delete=models.SET_NULL , null=True)
    node_title = models.CharField(max_length=20, blank=True, null=True)
    is_checked = models.BooleanField(default=False)
    mark_delete = models.BooleanField(default=False)





class ParentTask(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name =  models.CharField(max_length=20, null=True, blank=True)
    all_task_done = models.BooleanField(default=False)
    daily_done =  models.BooleanField(default=False)
    completed =  models.BooleanField(default=False)
    remainder =  models.CharField(max_length=20, null=True, blank=True)

class ListItem(BaseModel):
    parent_task = models.ForeignKey(ParentTask,on_delete=models.SET_NULL, null=True, blank=True)
    name =  models.CharField(max_length=20, null=True, blank=True)
    done =  models.BooleanField(default=False)
    remainder =  models.CharField(max_length=20, null=True, blank=True)
    
