from .serializers import LetterDesignSerializer
from django.contrib.auth.models import User
from core.models import LetterDesign
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated,AllowAny
from uuid import UUID

class LetterDesignViewSet(viewsets.ModelViewSet):
    serializer_class = LetterDesignSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'lc_id'

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


    # def retrieve(self, request, pk=None):
    #     pass
    
    #@csrf_exempt
    def update(self, request, lc_id=UUID):
        # Retrieve the object to update based on the lc_id from the URL
        # Ensure that the object belongs to the current user
        try:
            letter_design = self.get_queryset().get(lc_id=lc_id)
        except LetterDesign.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if letter_design.user != request.user:
            return Response({"detail": "You do not have permission to edit this letter."}, 
                             status=status.HTTP_403_FORBIDDEN)

        # 1. LOGGING: See exactly what is arriving
        print("DEBUG: Request Data Keys:", request.data.keys())
        print("DEBUG: State Data Content:", request.data.get('state_data'))

        # 2. Extract state_data specifically
        # If your JS sends it as an object, DRF JSONField handles it.
        # If your field is a TextField, you need to stringify in JS or here.
        incoming_state = request.data.get('state_data')
        # Serialize the data for the update
        serializer = self.get_serializer(letter_design, data=request.data)

        # Validate the serializer
        if serializer.is_valid():
            #serializer.validated_data['user'] = request.user
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass
