# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TextSearchSerializer

class TextSearchView(APIView):
    def post(self, request):
        serializer = TextSearchSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            keyword = serializer.validated_data['keyword']

            # Perform simple keyword search
            found = keyword.lower() in text.lower()

            return Response({
                'found': found,
                'message': 'Keyword found in text' if found else 'Keyword not found in text'
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
