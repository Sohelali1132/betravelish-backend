from django.contrib import admin
from .models import Trek

@admin.register(Trek)
class TrekAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'difficulty', 'price', 'is_active', 'created_at')
    list_filter = ('difficulty', 'is_active', 'created_at')
    search_fields = ('title', 'location', 'description')
