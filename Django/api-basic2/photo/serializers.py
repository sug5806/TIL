from rest_framework import serializers

from .models import Photo


class PhotoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['text', 'image']

    def create(self, validated_data):
        author = Photo.objects.create(**validated_data)

        return author


class PhotoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['text', 'image']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if value:
                setattr(instance, attr, value)
        instance.save()

        return instance


class PhotoDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
