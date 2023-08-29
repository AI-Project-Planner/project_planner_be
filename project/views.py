from django.shortcuts import render, get_object_or_404
from .models import Project
from user.models import User
from .serializers import ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import code, requests, json, dotenv, os

def generate_project(request, id):
    # Find user
    # if user is nil, return error
    user = User.objects.get(id=id)

    # Parse request
    parsed_request = json.loads(request.body)
    technologies = parsed_request['technologies']
    timeline = parsed_request['time']
    timeline_split = parsed_request['time'].split()
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

    # Question: how to rescue from errors when we can't parse the object the OpenAI returned
    ## Errors could potentially happen when the api doesn't close their json
    ## syntax: try, except
    ## Question about how and what to test?
    ### end to end testing, setting up a mock server to show the fulll request/repsonse
    # Question: how to test that our serializer is returning everything we are obliged to per the json contract
    # Question: how to setup more robust CircleCI integration instead of just 'build'

    parsed = response.json()
    #if response status code = 200 then...
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

    # Project.objects.create(name=name, description=description, steps=steps, features=features, interactions=interactions, colors=colors)
    # code.interact(local=dict(globals(), **locals()))
