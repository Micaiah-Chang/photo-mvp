from django.urls import path, include
from . import views




urlpatterns = [
    path(r'photos/', views.PhotoView.as_view(), name='photo_view'),
    path(r'albums/', views.AlbumView.as_view(), name='album_view')
]
