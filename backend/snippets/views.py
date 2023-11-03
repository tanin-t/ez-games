from snippets.models import Snippet, Highest
from snippets.serializers import SnippetSerializer, HighestSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
from django.http import JsonResponse


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
    highest = Highest.objects.filter(id=7)
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
   
   def put(self, request, id):
        print("id", id)
        
        validator = HighestSerializer(data=request.data)
        
        validator.is_valid(raise_exception=True)
        
        highest = Highest.objects.get(id=id)
        
        data = request.data
        print("---------------------", data, data["score"])
        
        highest.score = data["score"]
        highest.save()
        
        # Return a JSON response with the updated data
        response_data = {
            "id": highest.id,
            "score": highest.score,
            # Add other fields you want to include in the response
        }
        
        return JsonResponse(response_data)

       


    
