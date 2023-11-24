from django.shortcuts import get_object_or_404
from .models import User
from .serializers import ProfileSerializer, CustomRegisterSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework import status


@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def profile(request, username):
    user = get_user_model().objects.get(username=username)

    if request.method == 'GET':
        serializer = ProfileSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        if request.user != user:
            return Response({'detail': 'You do not have permission to edit this user.'}, status=403)

        serializer = ProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def register_user(request):
    serializer = CustomRegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save(request)
        duration = request.data.get('duration', 0)

        if duration <= 90000:
            personality_type = "급함"
        elif duration <= 180000:
            personality_type = "보통"
        else:
            personality_type = "느긋함"
        
        user.duration = duration
        user.save()

        return JsonResponse({"message": "User registered successfully", "personality_type": personality_type})
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)