from rest_framework import serializers

from .models import Comment, Like


class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class LikeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = "__all__"
