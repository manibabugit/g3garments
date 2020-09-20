from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .forms import *
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')



def upload_image(request): 
  
    if request.method == 'POST': 
        form = UploadImageForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = UploadImageForm() 
    return render(request, 'base/upload_image_form.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfully uploaded') 



def display_uploaded_images(request):
    if request.method == 'GET':

        # gettting all the objects of UploadImage
        images = UploadImage.objects.all()
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


''' testing git from vscode '''
