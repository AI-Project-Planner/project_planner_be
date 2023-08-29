from django.shortcuts import render, get_object_or_404
from .models import Project
from user.models import User
from .serializers import ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import code, requests, json

@api_view(['GET'])
def return_a_project(request, id):
    try: 
        project = Project.objects.get(id=id)
    except:
        return 'wrong'

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
    headers = { 'Authorization': 'Bearer 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' }
    response = requests.post('https://api.openai.com/v1/chat/completions', json=payload, headers=headers)
    x = response.json()
    y = x['choices'][0]['message']['content']
    z = json.loads(y)

    u = User.objects.create(name='Taylor Swift', email='erastour@gmail.com')
    steps = "\n".join(z['Steps'])
    features = "\n".join(z['Features'])
    interactions = "\n".join(z['Interactions'])
    colors = "\n".join(z['ColorPalette'])

    new_project = Project.objects.create(user=u, name=z['ProjectName'], description=z['Description'], steps=steps, features=features, interactions=interactions, colors=colors)
    # Add in collaborators && tagline && timeline

    code.interact(local=dict(globals(), **locals()))

    serializer = ProjectSerializer(project)
    return Response(Project.serialize_project(serializer, id), status=status.HTTP_200_OK)
    