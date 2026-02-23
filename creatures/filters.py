import django_filters
from .models import Creature

class CreatureFilter(django_filters.FilterSet):
    class Meta:
        model = Creature
        fields = {
         'danger_level': ['exact', 'gte', 'lte'],
         'is_sapient': ['exact'],
         'tags': ['exact'],
        }