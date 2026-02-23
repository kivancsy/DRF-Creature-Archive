from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, permissions
from .models import Creature, Tag
from .serializers import CreatureSerializer, TagSerializer
from .filters import CreatureFilter
from .permissions import IsOwnerOrReadOnly

class CreatureViewSet(viewsets.ModelViewSet):
    serializer_class = CreatureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = CreatureFilter
    search_fields = ['name', 'description', 'lore']

    def get_queryset(self):
        queryset = Creature.objects.all().order_by('-created_at')
        if self.request.query_params.get('mine') == 'true':
            queryset = queryset.filter(created_by=self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('id')
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]