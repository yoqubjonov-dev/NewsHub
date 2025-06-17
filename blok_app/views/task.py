from django.db.models import Avg
from  rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from blok_app.models import Task
from blok_app.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset =Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=False, methods=['get'])
    def top_rated(self, request):
        top_tasks = Task.objects.annotate(avg_rating=Avg('reviews__score')).order_by('-avg_rating')[
                    :5]  # eng yuqori 5 ta
        serializer = self.get_serializer(top_tasks, many=True)
        return Response(serializer.data)