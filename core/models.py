from django.db import models
import uuid
from accounts.models import User
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True ,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True



class SeoTags(BaseModel):
    keyword = models.CharField(max_length=50, blank=False, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.keyword


class LetterDesign(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='letter_design')
    state_data = models.JSONField(blank=True, null=True) # keep storing the user editor canvas changes and its value css,variable,state and context data.
    
    