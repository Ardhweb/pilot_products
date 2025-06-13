from django.db import models

# Create your models here.
from core.models import BaseModel
from django.contrib.auth import get_user_model
User = get_user_model()

class MyFirm(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='firms')
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)