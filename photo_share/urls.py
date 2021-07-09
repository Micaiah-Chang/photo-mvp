from django.urls import path, include
from . import views




urlpatterns = [
    path(r'photos/', views.PhotoView.as_view(), name='photo_view'),
    path(r'photos/<int:photo_id>/', views.IndividualPhotoView.as_view(), name='single_photo_view'),
    path(r'albums/', views.AlbumView.as_view(), name='album_view'),
    path(r'albums/<int:album_id>/', views.IndividualAlbumView.as_view(),
         name='single_album_view'),
    path(r'albums/<int:album_id>/add-photo/<int:photo_id>/', views.AddPhotoView.as_view(),
         name='add_photo'),
]
