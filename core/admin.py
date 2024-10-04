from django.contrib import admin

# Register your models here.
from .models import SeoTags

@admin.register(SeoTags)
class SeoTagAdmin(admin.ModelAdmin):
    list_display = ['keyword', 'created_at']