from .views import CommentModelViewSet, LikeModelViewSet
from rest_framework.routers import DefaultRouter

app_name = "comments"

router = DefaultRouter()

# comments
router.register("comments", CommentModelViewSet, basename="comments")
router.register("likes", LikeModelViewSet, basename="likes")

urlpatterns = []
urlpatterns += router.urls
