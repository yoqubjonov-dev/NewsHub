from rest_framework import viewsets
from blok_app.models import Comment
from blok_app.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer