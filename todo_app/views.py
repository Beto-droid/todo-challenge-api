from rest_framework import generics, viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .filters import TasksFilter
from .models import User, Tasks
from .serializers import UserSerializer, TasksSerializer
from django_filters.rest_framework import DjangoFilterBackend


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = None

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    # Json decode and encode
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]

    # noinspection SpellCheckingInspection
    filterset_class = TasksFilter
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]