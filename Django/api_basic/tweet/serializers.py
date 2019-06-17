from rest_framework import serializers

from .models import Tweet


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['author', 'text', ]


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['author', 'text', ]