from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import  UserManager
from django.utils.timezone import now
from datetime import timedelta
# Create your models here.
class User(AbstractUser):
    user_role = models.CharField(max_length=50,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = UserManager()
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Avoid conflict
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Avoid conflict
        blank=True,
    )


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.TextField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class EmailVerification(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     verification_code = models.PositiveIntegerField(null=True,  blank=True)
#     attempts = models.PositiveIntegerField(default=0, null=True,  blank=True)
#     max_attempts = models.IntegerField(default=3)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_expired = models.BooleanField(default=True)

#     def has_expired(self):
#         return now() > self.created_at + timedelta(hours=24)

#     def increment_attempts(self):
#         self.attempts += 1
#         if self.attempts >= self.max_attempts:
#             self.is_expired = False
#         self.save()
