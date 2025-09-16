from rest_framework import serializers
from core.models import LetterDesign

class LetterDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = LetterDesign
        fields = "__all__"