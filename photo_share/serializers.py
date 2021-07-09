from rest_framework import serializers
from . import models


class PhotoSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Photo
        fields = ['s3_file_url', 'creation_date', 'id']


class AlbumSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(required=False, many=True, read_only=True)


    class Meta:
        model = models.Album
        fields = ['name', 'creation_date', 'photos', 'id']
        depth = 1
