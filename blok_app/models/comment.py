from django.db import models
from .task import Task

class Comment(models.Model):
    title = models.ForeignKey(Task, on_delete=models.CASCADE,  related_name='reviews')
    content = models.TextField(blank=True, null=True)
    score = models.PositiveSmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title