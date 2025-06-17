from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blok_app.views import TaskViewSet, CommentViewSet

router =DefaultRouter()
router.register('task', TaskViewSet)
router.register('comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
