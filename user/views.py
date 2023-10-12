from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

@api_view(['GET'])
def show_user(request, id):
    user = User.objects.get(id=id)
    serializer = UserSerializer(user)
    return Response(User.serialize_user(serializer, user.id), status=status.HTTP_200_OK)

@api_view(['POST'])
def generate_user(request):
    parsed_request = json.loads(request.body)
    name = parsed_request['name']
    email = parsed_request['email']
    created_user = User.objects.create(name=name, email=email)
    serializer = UserSerializer(created_user)
    return Response(User.serialize_user(serializer, created_user.id), status=status.HTTP_201_CREATED)

@api_view(['POST'])
def find_or_create_user(request):
    parsed_request = json.loads(request.body)
    name = parsed_request['name']
    email = parsed_request['email']

    try:
      user = User.objects.get(email=email)
    except User.DoesNotExist:
      user = User.objects.create(name=name, email=email)
      serializer = UserSerializer(user)
      return Response(User.serialize_user(serializer, user.id), status=status.HTTP_201_CREATED)

    serializer = UserSerializer(user)
    return Response(User.serialize_user(serializer, user.id), status=status.HTTP_200_OK)