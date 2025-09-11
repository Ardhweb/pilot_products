from django.contrib import admin

# Register your models here.
from .models import SeoTags,LetterDesign

@admin.register(SeoTags)
class SeoTagAdmin(admin.ModelAdmin):
    list_display = ['keyword', 'created_at']

@admin.register(LetterDesign)
class LetterDesignAdmin(admin.ModelAdmin):
    list_display = ['id']