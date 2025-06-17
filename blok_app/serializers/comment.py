from rest_framework import serializers
from blok_app.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField(required=False, allow_null=True)
    class Meta:
        model = Comment
        fields = '__all__'

