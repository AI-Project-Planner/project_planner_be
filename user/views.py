from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

@api_view(['GET'])
def show_user(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        response = {
            "Error": "User ID not found",
            "Status": 404
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    return Response(User.serialize_user(serializer, user.id), status=status.HTTP_200_OK)

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