from rest_framework import generics, viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .filters import TasksFilter
from .models import User, Tasks
from .serializers import UserSerializer, TasksSerializer, TasksCreateSerializer, TasksUpdateSerializer, UserRegistrationSerializer
from django_filters.rest_framework import DjangoFilterBackend


class RegistrationAPIView(generics.CreateAPIView):
    """
    Simple registration View
    """
    serializer_class = UserRegistrationSerializer
    model = User
    permission_classes = [AllowAny]

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

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

    search_fields = ['created_at', 'description']  # for django filter.SearchFilter
    ordering_fields = ['created_at']  # For filters.OrderingFilter

    # This will save the task to the user that created it.
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # Override get, shows only users tasks or admin
    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)
        return qs

    # This will "change" the serializer used, dep on REST request
    def get_serializer_class(self):
        if self.action in ['create']:
            return TasksCreateSerializer
        if self.action in ['update']:
            return TasksUpdateSerializer
        return super().get_serializer_class()

