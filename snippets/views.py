from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics
class SnippetList(generics.ListCreateAPIView):
    '''
    List code snippets or Create a new one.
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer



class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, Update or Delete a code snippet.
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


    

    