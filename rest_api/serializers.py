from rest_framework import serializers
from aiapp.models  import CoverLetter ,CoverLetterHistory

class CoverLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverLetter
        fields = ['id', 'description', 'content', 'finalized', 'created_at']
        read_only_fields = ['id', 'finalized', 'created_at']

class CoverLetterHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverLetterHistory
        fields = ['id', 'cover_letter', 'user', 'description', 'generated_content', 'timestamp']
        read_only_fields = ['id', 'timestamp']
