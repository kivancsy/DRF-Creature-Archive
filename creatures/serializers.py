from rest_framework import serializers
from .models import Creature, Tag
from django.contrib.auth.models import User

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
   
        
class CreatureSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Tag.objects.all(), write_only=True, source='tags'
    )
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Creature
        fields = ['id', 'name', 'description', 'lore',
                  'danger_level', 'habitat', 'is_sapient', 
                  'tags', 'tag_ids', 'created_by', 'created_at', 'updated_at'
                 ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user