from django.shortcuts import render
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import  User
from django.http import HttpResponse
import requests
# Create your views here.

def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password1']:
            #REGISTRAR USUARIO
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('Usuario creado satisfactoriamente')
            
            except requests.exceptions.RequestException as errorRequest:
                 return HttpResponse(f'Error en los datos {errorRequest}')
              
        else:        
            return HttpResponse('No se encuentra el usuario')
    else:
        return render(request, 'signup.html',{
            'form': UserCreationForm
        }) 
    
    