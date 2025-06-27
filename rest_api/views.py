from aiapp.models import CoverLetter,CoverLetterHistory
from .serializers import CoverLetterSerializer,CoverLetterHistorySerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def draft_for_letter(request):
    user = request.user
    data = request.data.copy()  # make mutable

    # Fix description if list (from form data)
    description = data.get('description')
    if isinstance(description, list):
        data['description'] = description[0]

    # Assign dummy data for required fields not sent by the form
    if not data.get('title'):
        data['title'] = 'Undefind Title'
    if not data.get('content'):
        data['content'] = 'undefind Content'

    print(f"Received data from user {user}: {data}")

    serializer = CoverLetterSerializer(data=data)
    if not serializer.is_valid():
        print("Serializer errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Save or process your validated data
    cover_letter = serializer.save(user=user, finalized=False)

    # For now just return the validated data as response
    return Response({
        "id": cover_letter.id,
        "title": serializer.validated_data.get('title'),
        "content": serializer.validated_data.get('content'),
        "description": serializer.validated_data.get('description'),
    }, status=status.HTTP_200_OK)



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def finalize_letter(request):
    content = request.data.get("content")
    cover_letter_id = request.data.get("cover_letter_id")

    if not content or not cover_letter_id:
        return Response({"error": "Invalid input"}, status=400)

    try:
        cover_letter = CoverLetter.objects.get(id=cover_letter_id, user=request.user)
        cover_letter.content = content
        cover_letter.finalized = True
        cover_letter.save()

        return Response({"message": "Cover letter finalized."}, status=200)

    except CoverLetter.DoesNotExist:
        return Response({"error": "Cover letter not found"}, status=404)
