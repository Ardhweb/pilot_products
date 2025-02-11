from django.contrib.auth.backends import ModelBackend
from accounts.models import User  # Import your custom User model

class CustomBackend(ModelBackend):
    """Custom authentication backend that allows login using email instead of username."""
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):  # Check password manually
                return user
        except User.DoesNotExist:
            return None
        return None
