from rest_framework import serializers
from . import models


class AlbumSerializer(serializers.ModelSerializer):
    photos = serializers.PrimaryKeyRelatedField(required=False, many=True)

    class Meta:
        model = models.Album
        fields = ['name', 'creation_date', 'photos']


class PhotoSerializer(serializers.ModelSerializer):



    class Meta:
        model = models.Photo
        fields = ['s3_file_url', 'creation_date']
