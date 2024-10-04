from django.db import models

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
    