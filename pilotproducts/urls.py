"""
URL configuration for pilotproducts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static 
from django.conf import settings
from django.conf.urls.static import static
from .api_routers import router as main_router
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .config.serverconfig import server_stage
from django.urls import re_path
from django.views.defaults import page_not_found

# Set up Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="PilotProducts API Docs",
        default_version='v1',
        description="API documentation for managing letter designs.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@letterdesign.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns+=static(settings.STATIC_URL,
document_root=settings.STATIC_ROOT)
print(settings.STATIC_URL)
"""
SECURITY CONFIGURATION: Production vs. Development Environment
--------------------------------------------------------------
- DEVELOPMENT: Allows access to all app endpoints, test views, and Django templates
  for feature verification and debugging.
- PRODUCTION: Restricts access to API and Admin endpoints only. 
- PURPOSE: Prevents exposure of 'unfitted' test code and template logic to the public.
  By isolating the backend, we reduce the attack surface and prevent exploitation 
  of internal development routes.
"""
if settings.DEBUG and server_stage == 'dev':
    urlpatterns += [
        path('api-auth/', include('rest_framework.urls')),
        path('api/', include(main_router.urls)),
        path('admin/', admin.site.urls),
        path('', include("core.urls")),
        path('accounts/', include("accounts.urls")),
        path('accounts/', include('allauth.urls')),
        path('api-docs', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    ]
else:
    urlpatterns += [
    # path('rest-api/',include('rest_api.urls', namespace="rest_api")),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(main_router.urls)),
    ]

handler404 = 'core.views.error_404'

if not settings.DEBUG or server_stage != 'dev':
    urlpatterns += [
        # This returns the standard Django 404 page
        re_path(r'^.*$', lambda request: page_not_found(request, exception=Exception("Page not Found"))),
    ]

