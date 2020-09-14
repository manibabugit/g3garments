from django.db import models

# Create your models here.

class UploadImage(models.Model): 
    name = models.CharField(max_length=50) 
    Img = models.ImageField(upload_to='images/')
    uploaded = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name 