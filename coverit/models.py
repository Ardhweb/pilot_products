from django.db import models
from core.models import BaseModel
# Create your models here.

class CoverLetter(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    contents = models.TextField(blank=True, null=True)
    mark_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    