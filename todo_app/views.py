from django.contrib.auth import login
from rest_framework import generics, viewsets, filters, status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

from .filters import TasksFilter
from .models import User, Tasks
from .serializers import UserSerializer, TasksSerializer, TasksCreateSerializer, TasksUpdateSerializer, \
    UserRegistrationSerializer, UserLoginSerializer
from django_filters.rest_framework import DjangoFilterBackend


class RegistrationAPIView(generics.CreateAPIView):
    """
    Simple registration View
    """
    serializer_class = UserRegistrationSerializer
    model = User
    permission_classes = [AllowAny]

class LoginAPIView(generics.GenericAPIView):
    """
    API View to log in a user via session authentication.
    """
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(
            {"user_status": "Logged in successfully", "username": user.username},
            status=status.HTTP_200_OK,
        )

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

    # For letting the admin/staff to bypass the status changes
    # He should be able to do this.
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    # This will save the task to the user that created it.
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # This will "change" the serializer used, dep on REST request
    def get_serializer_class(self):
        if self.action in ['create']:
            return TasksCreateSerializer
        if self.action in ['update', 'partial_update']:
            return TasksUpdateSerializer
        return super().get_serializer_class()

    # Override get, shows only users tasks or admin
    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)
        return qs

