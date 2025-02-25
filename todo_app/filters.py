import django_filters

from .models import Tasks

class TasksFilter(django_filters.FilterSet):
    created_at = django_filters.DateFilter(field_name='created_at__date')  # this is necessary bc if not it defaults at midnight
    completed_at = django_filters.DateFilter(field_name='completed_at__date')
    started_at = django_filters.DateFilter(field_name='started_at__date')
    class Meta:
        model = Tasks
        fields = {
            'status' : ['exact'],
            'title' : ['icontains'],
            'description' : ['icontains'],
            'created_at': ['lt', 'gt', 'exact', 'range'],
            'started_at': ['lt', 'gt', 'exact', 'range'],
            'completed_at': ['lt', 'gt', 'exact', 'range'],
        }