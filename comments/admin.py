from django.contrib import admin
from .models import Comment, Like

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "author",
        "short_text",
        "likes_count",
        "id",
    ]

    def short_text(self, obj):
        return obj.text[:50]  # Returns the first 30 characters of the text

    short_text.short_description = "Text Preview"  # Display name in the admin panel

    def likes_count(self, obj):
        return obj.likes.count()  # Returns the number of users who liked the comment

    likes_count.short_description = "Likes Count"  # Display name in the admin panel

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "comment",
        "id",
    ]
