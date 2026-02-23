from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, permissions, status
from rest_framework.response import Response
from .models import Creature, Tag
from .serializers import CreatureSerializer, RegisterSerializer, TagSerializer
from .filters import CreatureFilter
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

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
    
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)