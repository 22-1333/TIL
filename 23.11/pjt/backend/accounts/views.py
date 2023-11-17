from django.shortcuts import get_object_or_404

from .models import User
from .serializers import ProfileSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def profile(request, username):
    serializer = ProfileSerializer(get_object_or_404(User, username=username))
    return Response(serializer.data)
