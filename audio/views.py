from rest_framework.viewsets import ModelViewSet

from core.paginations import  DefaultLimitOffSetPagination
from .serializers import AudioListSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticated, AllowAny
from .models import Audio



class AudioModelViewSet(ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioListSerializer
    pagination_class = DefaultLimitOffSetPagination
    permission_classes = [AllowAny]
