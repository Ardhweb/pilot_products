import os
import uuid
from django.db import models
from accounts.models import User
def upload_to_user_folder(instance, filename):
    ext = filename.split('.')[-1]
    user_id = instance.user.id  # or username: instance.user.username
    encoded_name = f"{uuid.uuid4().hex}.{ext}"
    # Store file under media/uploads/user_<id>/<encoded_filename>
    return os.path.join('uploads', f'user_{user_id}', encoded_name)

class UploadAnalyzedFile(models.Model):
    STATUS_CHOICES = [
        (0, 'Pending'),
        (1, 'Processing'),
        (2, 'Processed'),
        (3, 'Failed'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='analyzed_files'
    )
    file = models.FileField(upload_to=upload_to_user_folder)
    original_filename = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    file_type = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.original_filename
