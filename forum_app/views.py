from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Topic, Comment, Reply
from .serializers import TopicSerializer, CommentSerializer, ReplySerializer

class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class ReplyViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [IsAuthenticated]
