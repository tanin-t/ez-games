from snippets.models import Snippet, Highest
from snippets.serializers import SnippetSerializer, HighestSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = list(Snippet.objects.all())
        random.shuffle(snippets)  # Shuffle the list in-place
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)


class HighestList(APIView):
   def get(self, request):
    highest = Highest.objects.all()
    if highest:
            serializer_high = HighestSerializer(highest, many=True)
           
            return Response(serializer_high.data)
    else:
        # Handle the case when the list is empty
        return Response([], status=status.HTTP_204_NO_CONTENT)
   

   def post(self, request):
        serializer = HighestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
