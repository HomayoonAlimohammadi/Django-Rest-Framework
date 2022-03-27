from rest_framework import serializers
from .models import Snippet
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    queryset = Snippet.objects.all()
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=queryset)

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']