from .models import Project
from user.models import User
from .serializers import ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests, json, os, code

@api_view(['GET', 'POST'])
def generate_project(request, id):
    if request.method == 'POST':
        # Find user
        try:
            user = User.objects.get(id=id)

        except User.DoesNotExist:
            response = {
                "Error": "User ID not found",
                "Status": 404
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        # Parse request
        parsed_request = json.loads(request.body)
        technologies = parsed_request['technologies']
        timeline = parsed_request['time']
        timeline_split = parsed_request['time'].split()[-1]
        timeline_integer = parsed_request['time'].split()[0]
        collaborators = parsed_request['collaborators']
        stack = parsed_request['type']

        # Interpolate request values into API call
        payload = {
            "model": "gpt-3.5-turbo-16k",
            "messages": [
                {
                "role": "user",
                "content": f"Create a plan for a {stack} application using {technologies}. I have {timeline} to build this application. Include additional feature ideas that the application could have. There will be {collaborators} people working on this project.",
                "role": "system",
                "content": "In this plan, please include a name for the application, a schedule for project completion, a plan for how the users would interact with the application, and provide an example interaction. Include a color palette with 6 colors for this app. Provide your new response in JSON format with the following Keys: ProjectName, Description, Steps, Features, Interactions, ColorPalette, and Tagline. Tagline should be a five word summary of the project description. Steps, Features, Interaction and ColorPalette values should come back as an array. Any value inside of an array should not be numbered."
                }
            ]
        }

        headers = { 'Authorization': os.environ['OPEN_API_KEY'] }
        response = requests.post('https://api.openai.com/v1/chat/completions', json=payload, headers=headers)

        if response.status_code==200:
            # refactor: error handling: if response status code = 200 then...
            parsed = response.json()
            project = parsed['choices'][0]['message']['content']
            parsed_project = json.loads(project)

            name = parsed_project['ProjectName']
            description = parsed_project['Description']
            tagline = parsed_project['Tagline']
            steps = "\n".join(parsed_project['Steps'])
            features = "\n".join(parsed_project['Features'])
            interactions = "\n".join(parsed_project['Interactions'])
            colors = "\n".join(parsed_project['ColorPalette'])

            # From the request, we need to save the timeline_split and collaborators to the DB entry
            project = Project.objects.create(name=name, description=description, steps=steps, features=features, interactions=interactions, colors=colors, user_id=user, collaborators=collaborators, timeline=timeline_split, timeline_int=timeline_integer, tagline=tagline, technologies=technologies)

            # Serialize the project
            serializer = ProjectSerializer(project)
            return Response(Project.serialize_project(serializer, project.id), status=status.HTTP_200_OK)
        else:
            response = {
                "Error": "Server is Down",
                "Status": 503
            }
            return Response(response, status=status.HTTP_503_SERVICE_UNAVAILABLE)

    elif request.method == 'GET':
        try:
            User.objects.get(id=id)
        except User.objects.DoesNotExist:
            response = {
                "Error": "User ID not found",
                "Status": 404
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        projects = Project.objects.all()
        return Response(Project.serialize_all_projects(projects), status=status.HTTP_200_OK)

@api_view(['PUT', 'PATCH', 'DELETE'])
def update_project(request, user_id, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        response = {
            "Error": "Project or User ID not found",
            "Status": 404
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        project_serializer = ProjectSerializer(project, data=request.data)
        if project_serializer.is_valid():
            project_serializer.save()
            return Response(Project.serialize_project(project_serializer, project_id), status=status.HTTP_202_ACCEPTED)
        else:
            response = {
                "Error": f"{project_serializer.errors}",
                "Status": 400
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        parsed_request = json.loads(request.body)
        saved_status = parsed_request['saved']
        if saved_status=='true':
            saved_status=True
        elif saved_status=='false':
            saved_status=False
        project.saved=saved_status
        project.save()
        serializer = ProjectSerializer(project)
        return Response(Project.serialize_project(serializer, project_id), status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        try:
            project = Project.objects.get(id=project_id)
            project.delete()
            return Response({"messages": "Project with id " + str(project_id) + " was deleted."}, status=status.HTTP_200_OK)
        except Project.DoesNotExist:
            response = {
                "Error": "Project ID not found",
                "Status": 404
            }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
