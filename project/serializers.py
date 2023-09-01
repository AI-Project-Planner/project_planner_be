from rest_framework import serializers
from project.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['user_id', 'name', 'description', 'steps', 'features', 'technologies', 'colors', 'interactions', 'timeline', 'timeline_int', 'saved', 'tagline', 'collaborators']