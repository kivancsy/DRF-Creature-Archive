from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Creature(models.Model):
    class DangerLevel(models.IntegerChoices):
        HARMLESS = 1
        LOW = 2
        MODERATE = 3
        HIGH = 4
        APEX = 5
        
    name = models.CharField(max_length=100)
    description = models.TextField()
    lore = models.TextField(null=True)
    danger_level = models.IntegerField(choices=DangerLevel.choices)
    habitat = models.CharField(max_length=100)
    is_sapient = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creatures')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
