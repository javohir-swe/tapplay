from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "author",
        "text",
        "likes_count",
        "id",
    ]
    # list_filter = ["is_staff", "is_active", "is_verified"]
    def likes_count(self, obj):
        return obj.likes.count()  # Returns the number of users who liked the comment

    likes_count.short_description = "Likes Count"  # Display name in the admin panel
