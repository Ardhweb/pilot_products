"""
WSGI config for pilot_products project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pilot_products.settings')

application = get_wsgi_application()

# import sys

# # Add your project directory to the Python path
# project_home = '/home/yourusername/yourprojectname'
# if project_home not in sys.path:
#     sys.path.append(project_home)

# # Set the settings module for the Django project
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yourprojectname.settings')

# # Activate your virtual environment (if you are using one)
# activate_this = os.path.join(project_home, 'venv/bin/activate_this.py')
# with open(activate_this) as file_:
#     exec(file_.read(), dict(__file__=activate_this))

# # Import and create the WSGI application
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
