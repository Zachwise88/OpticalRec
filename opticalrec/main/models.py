from django.db import models
from .validators import *

# Create your models here.

class Video(models.Model):
    name= models.CharField(max_length=500)
    userId=models.IntegerField(null=True, blank=True)
    videoFile= models.FileField(upload_to='videos/', validators=[validate_file_ext], null=True, verbose_name="")
    uploadedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ": " + str(self.videofile)

    def delete(self):
        self.videoFile.delete()
        self.videoFile="Deleted"
        self.save()

class Frame(models.Model):
    vidId=models.IntegerField()
    userId=models.IntegerField()
    frameFile=models.ImageField(upload_to="frames/", blank=True)
    frameNum=models.IntegerField()