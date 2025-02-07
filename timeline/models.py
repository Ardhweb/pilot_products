from django.db import models
from core.models import BaseModel
# Create your models here.
class Timeline(BaseModel):
    title = models.CharField(max_length=50, blank=True, null=True)
    mark_delete = models.BooleanField(default=False)
    

class TimelineNode(BaseModel):
    time_line =  models.ForeignKey(Timeline, on_delete=models.SET_NULL , null=True)
    node_title = models.CharField(max_length=20, blank=True, null=True)
    is_checked = models.BooleanField(default=False)
    mark_delete = models.BooleanField(default=False)


class DailyParent(BaseModel):
    name =  models.CharField(max_length=20, null=True, blank=True)
    remainder =  models.CharField(max_length=20, null=True, blank=True)


class AnchorCheckPoint(BaseModel):
    all_task_done = models.BooleanField(default=False)
    daily_done =  models.BooleanField(default=False)
    dailyparent = models.ForeignKey(DailyParent,on_delete=models.SET_NULL, null=True, blank=True)
    completed =  models.BooleanField(default=False)

class ListItem(BaseModel):
    anchorcheckpoint = models.ForeignKey(AnchorCheckPoint,on_delete=models.SET_NULL, null=True, blank=True)
    name =  models.CharField(max_length=20, null=True, blank=True)
    done =  models.BooleanField(default=False)
    remainder =  models.CharField(max_length=20, null=True, blank=True)
    
