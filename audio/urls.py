from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import AudioModelViewSet


app_name = "audio"
router = DefaultRouter()

# audios
router.register("audio", AudioModelViewSet, basename="audio")

urlpatterns = []

urlpatterns += router.urls
