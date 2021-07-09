from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as rest_status

from . import serializers
from . import models




class PhotoView(APIView):


    def get(self, request):
        user = request.user

        photos = models.Photo.objects.filter(user=user)
        serializer = serializers.PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        data = request.data
        serializer = serializers.PhotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=rest_status.HTTP_201_CREATED)
        else:
            errors = serializer.errors
            return Response(errors, status=rest_status.HTTP_400_BAD_REQUEST)

class IndividualPhotoView(APIView):


    def get(self, request, photo_id):
        user = request.user

        photo = get_object_or_404(models.Photo, user=user, id=photo_id)
        serializer = serializers.PhotoSerializer(photo)
        return Response(serializer.data)

    def delete(self, request, photo_id):
        user, data = request.user, request.data
        photo = models.Photo.objects.filter(user=user, id=photo_id)
        if photo.exists():
            photo.delete()
            return Response({}, status=rest_status.HTTP_204_NO_CONTENT)
        else:
            error = {"detail": "Photo does not exist."}
            return Response(error, status=rest_status.HTTTP_404_NOT_FOUND)

class AlbumView(APIView):

    def get(self, request):
        user = request.user
        albums = models.Album.objects.filter(user=user)
        serializer = serializers.AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        data = request.data
        serializer = serializers.AlbumSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=rest_status.HTTP_201_CREATED)
        else:
            errors = serializer.errors
            return Response(errors, status=rest_status.HTTP_400_BAD_REQUEST)

class IndividualAlbumView(APIView):

    def get(self, request, album_id):
        user = request.user
        album = get_object_or_404(models.Album, user=user, id=album_id)
        serializer = serializers.AlbumSerializer(album)
        return Response(serializer.data)

    def patch(self, request, album_id):
        user = request.user
        album = get_object_or_404(models.Album, user=user, id=album_id)
        serializer = serializers.AlbumSerializer(album, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.datax, status=rest_status.HTTP_200_OK)
        else:
            errors = serializer.errors
            return Response(errors, status=rest_status.HTTP_400_BAD_REQUEST)

class AddPhotoView(APIView):

    def put(self, request, album_id, photo_id):
        user, data = request.user, request.data

        album = get_object_or_404(models.Album, id=album_id, user=user)
        photo = get_object_or_404(models.Photo, id=photo_id, user=user)

        album.photos.add(photo)

        serializer = serializers.AlbumSerializer(album)
        return Response(serializer.data,
                        status=rest_status.HTTP_200_OK)

# Create album has photos as optional
# retrieve album has all the photo information (at least URL) Do not need to solve n+1 join
# Add photo to an album
# edit on album ability


# viewset creating photos and albums for the right user
# do not override create method.

# only returning

# do not need to retrieve photo
