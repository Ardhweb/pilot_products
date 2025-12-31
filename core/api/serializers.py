from rest_framework import serializers
from core.models import LetterDesign

class LetterDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = LetterDesign
        fields = ['state_data']

    # def update(self, instance, validated_data):
    #     # Ensure the user is automatically set to the currently logged-in user
    #     user = self.context['request'].user  # Get the logged-in user from the request context
    #     validated_data['user'] = user  # Set the user field to the logged-in user

    #     # Call the parent class's update method to actually update the instance
    #     return super().update(instance, validated_data)