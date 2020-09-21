from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from base.models import UploadImage, UploadHoodiesImage, UploadJeansImage, UploadShirtsImage, UploadTracksImage
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')


def upload_image(request):
    print(request)
    if request.method == 'POST':
        image_file = request.FILES['image_file']
        if settings.USE_S3:
            upload = UploadImage(file=image_file)
            upload.save()
            image_url = upload.file.url
        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
        return render(request, 'base/upload_image_form.html', {
            'image_url': image_url
        })
    return render(request, 'base/upload_image_form.html')
  
def upload_jeans_image(request):
    print(request)
    if request.method == 'POST':
        image_file = request.FILES['image_file']
        if settings.USE_S3:
            upload = UploadJeansImage(file=image_file)
            upload.save()
            image_url = upload.file.url
        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
        return render(request, 'base/upload_jeans.html', {
            'image_url': image_url
        })
    return render(request, 'base/upload_jeans.html')  
    

def upload_shirts_image(request):
    print(request)
    if request.method == 'POST':
        image_file = request.FILES['image_file']
        if settings.USE_S3:
            upload = UploadShirtsImage(file=image_file)
            upload.save()
            image_url = upload.file.url
        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
        return render(request, 'base/upload_shirts.html', {
            'image_url': image_url
        })
    return render(request, 'base/upload_shirts.html')  


def upload_hoodies_image(request):
    print(request)
    if request.method == 'POST':
        image_file = request.FILES['image_file']
        if settings.USE_S3:
            upload = UploadHoodiesImage(file=image_file)
            upload.save()
            image_url = upload.file.url
        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
        return render(request, 'base/upload_hoodies.html', {
            'image_url': image_url
        })
    return render(request, 'base/upload_hoodies.html')  

def upload_tracks_image(request):
    print(request)
    if request.method == 'POST':
        image_file = request.FILES['image_file']
        if settings.USE_S3:
            upload = UploadTracksImage(file=image_file)
            upload.save()
            image_url = upload.file.url
        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
        return render(request, 'base/upload_tracks.html', {
            'image_url': image_url
        })
    return render(request, 'base/upload_tracks.html')  

def success(request): 
    return HttpResponse('successfully uploaded') 



def display_uploaded_images(request):
    if request.method == 'GET':

        # gettting all the objects of UploadImage
        images = UploadImage.objects.all()
        return render(request, 'base/display_uploaded_images.html', {'display_uploaded_images': images})


def list_jeans(request):
    if request.method == 'GET':

        # gettting all the objects of UploadImage
        images = UploadJeansImage.objects.all()
        return render(request, 'base/display_uploaded_images.html', {'display_uploaded_images': images})

def list_shirts(request):
    if request.method == 'GET':

        # gettting all the objects of UploadImage
        images = UploadShirtsImage.objects.all()
        return render(request, 'base/display_uploaded_images.html', {'display_uploaded_images': images})

def list_hoodies(request):
    if request.method == 'GET':

        # gettting all the objects of UploadImage
        images = UploadHoodiesImage.objects.all()
        return render(request, 'base/display_uploaded_images.html', {'display_uploaded_images': images})

def list_tracks(request):
    if request.method == 'GET':

        # gettting all the objects of UploadImage
        images = UploadTracksImage.objects.all()
        return render(request, 'base/display_uploaded_images.html', {'display_uploaded_images': images})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
      return render(request, 'base/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'base/loginuser.html', {'form': AuthenticationForm(), 'error': 'username password didnot match'} )
        else:
            login(request, user)
            return redirect('home') 


