from rest_framework import serializers
from snippets.models import Snippet, Highest


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = "__all__"


class HighestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highest
        fields = "__all__"
