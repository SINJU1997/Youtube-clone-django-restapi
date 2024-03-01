from django.db import models

# Create your models here.
class Youtubecl(models.Model):
    title=models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    channel = models.CharField(max_length=255)
    views= models.CharField(max_length=100)