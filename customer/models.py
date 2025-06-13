from django.db import models
from core.models import BaseModel
from firm.models import MyFirm
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Customer(BaseModel):
    full_name = models.CharField(max_length=20, blank=False, null=False, verbose_name='Your customer name')
    firm = models.ForeignKey(MyFirm, related_name='firms_customer', on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, blank=True,null=True)
    cell_phone = models.CharField(max_length=16,blank=True, null=True)
    tel_phone = models.CharField(max_length=16, blank=True, null=True)
