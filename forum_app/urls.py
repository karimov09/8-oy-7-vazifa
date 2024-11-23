from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TopicViewSet, CommentViewSet, ReplyViewSet

router = DefaultRouter()
router.register('topics', TopicViewSet)
router.register('comments', CommentViewSet)
router.register('replies', ReplyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
