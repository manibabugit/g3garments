from django.db import models
from g3garments.storage_backends import PublicMediaStorage

# Create your models here.

class UploadImage(models.Model): 
    file = models.FileField(storage=PublicMediaStorage())
    uploaded = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.file.name


class UploadJeansImage(models.Model): 
    file = models.FileField(storage=PublicMediaStorage())
    uploaded = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.file.name

class UploadShirtsImage(models.Model): 
    file = models.FileField(storage=PublicMediaStorage())
    uploaded = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.file.name

class UploadHoodiesImage(models.Model): 
    file = models.FileField(storage=PublicMediaStorage())
    uploaded = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.file.name

class UploadTracksImage(models.Model): 
    file = models.FileField(storage=PublicMediaStorage())
    uploaded = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.file.name