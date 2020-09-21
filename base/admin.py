from django.contrib import admin
from .models import UploadImage, UploadHoodiesImage, UploadJeansImage, UploadShirtsImage, UploadTracksImage
# Register your models here.
admin.site.register(UploadImage)
admin.site.register(UploadJeansImage)
admin.site.register(UploadShirtsImage)
admin.site.register(UploadHoodiesImage)
admin.site.register(UploadTracksImage)