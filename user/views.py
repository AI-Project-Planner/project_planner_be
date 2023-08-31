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
