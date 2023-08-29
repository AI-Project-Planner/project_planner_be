from rest_framework import serializers
from project.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['user_id', 'name', 'description', 'steps', 'features', 'colors', 'interactions', 'timeline', 'saved', 'tagline', 'collaborators']