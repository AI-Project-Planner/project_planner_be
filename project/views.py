from django.shortcuts import render, get_object_or_404
from .models import Project
from user.models import User
from .serializers import ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import code, requests, json

def generate_project(request, id):
    # Question: how do we take from the payload/request body?
    response = c.get(f"/api/v1/projects/{p.id}/")
    self.assertEqual(response.status_code, 200)

    returned_project = json.loads(response.content)["data"]

    payload = {
        "model": "gpt-3.5-turbo-16k",
        "messages": [
            {
            "role": "user",
            "content": "Create a plan for a full stack application using react, typescript, and express. I have 60 days to build this application. Include additional feature ideas that the application could have. There will be 8 people working on this project.",
            "role": "system",
            "content": "In this plan, please include a name for the application, a schedule for project completion, a plan for how the users would interact with the application, and provide an example interaction. Include a color palette with 6 colors for this app. Provide your new response in JSON format with the following Keys: ProjectName, Description, Steps, Features, Interactions, ColorPalette, and Tagline. Tagline should be a five word summary of the project description. Steps, Features, Interaction and ColorPalette values should come back as an array. Any value inside of an array should not be numbered."
            }
        ]
    }
