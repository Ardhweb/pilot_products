from .serializers import LetterDesignSerializer
from django.contrib.auth.models import User
from core.models import LetterDesign
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

class LetterDesignViewSet(viewsets.ModelViewSet):
    serializer_class = LetterDesignSerializer

    # Override `get_queryset` to only return objects for the authenticated user
    def get_queryset(self):
        return LetterDesign.objects.filter(user=self.request.user)
    
    @swagger_auto_schema(operation_description="Get all the design related current user .")
    def list(self, request, *args, **kwargs):
        # Get the queryset filtered for the current user
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Create a new letter design")
    def create(self, request, *args, **kwargs):
        # Create a new LetterDesign instance for the current user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Automatically set the user to the current authenticated user
        if 'user' not in serializer.validated_data:
            serializer.validated_data['user'] = request.user
        
        # Save the new design
        self.perform_create(serializer)

        # Return the response with the newly created design
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
