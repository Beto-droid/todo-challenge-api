from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter

from .views import RegistrationAPIView, LoginAPIView

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('register/', RegistrationAPIView.as_view(), name='registration'),
    path('login/', LoginAPIView.as_view())
]

router = DefaultRouter()
router.register('tasks', views.TaskViewSet)
urlpatterns += router.urls