import os
import sys
import django

# 1. Add Django project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# 2. Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# 3. Setup Django
django.setup()

# Now import Django models
from apps.users.models import User

from fastapi import FastAPI

app = FastAPI()

@app.get("/services/")
def get_status():
    return {"status":"Service Running"}
