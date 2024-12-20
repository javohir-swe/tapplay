from django.contrib import admin
from .models import Audio

@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "total_time",
        "status",
        "id",
    ]
    list_filter = ["author", "status"]
