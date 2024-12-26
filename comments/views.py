from rest_framework.viewsets import ModelViewSet

from utils.paginations import DefaultLimitOffSetPagination
from .serializers import CommentListSerializer, LikeListSerializer
from rest_framework.permissions import AllowAny
from .models import Comment, Like



class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    pagination_class = DefaultLimitOffSetPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        Return a queryset filtered by `audio_id` if provided as a query parameter.
        Otherwise, return all comments.
        """
        queryset = Comment.objects.all()
        audio_id = self.request.query_params.get('audio_id')
        if audio_id:
            queryset = queryset.filter(audio_id=audio_id)
        return queryset


class LikeModelViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeListSerializer
    pagination_class = DefaultLimitOffSetPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        Return a queryset filtered by `comment` if provided as a query parameter.
        Otherwise, return all Likes.
        """
        queryset = Like.objects.all()
        comment_id = self.request.query_params.get('comment_id')
        if comment_id:
            queryset = queryset.filter(comment=comment_id)
        return queryset