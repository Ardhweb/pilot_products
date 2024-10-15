from django.db import models
from core.models import BaseModel
# Create your models here.
from django.contrib.auth.models import User


class CoverLetter(BaseModel):
    title = models.CharField(max_length=50, blank=True, null=True)
    contents = models.TextField(blank=True, null=True)
    mark_delete = models.BooleanField(default=False)
    candidate = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    public = models.BooleanField(default=False)
    private = models.BooleanField(default=True)
    shareable_url = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.title
    