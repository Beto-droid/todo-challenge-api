from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter

from .views import RegistrationAPIView

urlpatterns = [
    path('users/', views.UserListView.as_view()),
    path('register/', RegistrationAPIView.as_view()),
]

router = DefaultRouter()
router.register('tasks', views.TaskViewSet)
urlpatterns += router.urls