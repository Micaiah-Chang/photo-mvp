from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    s3_file_url = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)

class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(null=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    photos = models.ManyToManyField(Photo, related_name='albums')
