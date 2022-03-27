from .models import Snippet
from django.contrib.auth.models import User
from .serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all() ## Why .all()?? shouldn't be .get(pk=pk) ?
    serializer_class = UserSerializer


class SnippetList(generics.ListCreateAPIView):
    '''
    List code snippets or Create a new one.
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, Update or Delete a code snippet.
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


    

    