import django_filters

from .models import Tasks

class TasksFilter(django_filters.FilterSet):
    created_at = django_filters.DateFilter(field_name='created_at__date')  # this is necessary bc if not it defaults at midnight
    class Meta:
        model = Tasks
        fields = {
            'description' : ['icontains'],
            'created_at': ['lt', 'gt', 'icontains', 'range'],
        }