from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from .form import signupForm
from django.contrib.auth import authenticate, login
# Create your views here.
def register_user(request):
    fm = signupForm()
    context = {
        'form':fm
    }
    if request.method == 'POST':
        fm = signupForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponse('user registraion is sucessful')
    
    return render(request, 'user.html',context)



def register_user(request):
    fm = AuthenticationForm()
    context = {
        'form':fm
    }
    if request.method == 'POST':
        fm = AuthenticationForm(data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user_object = authenticate(request, username=username, password=password)
            if user_object is not None:
                if user_object.is_authenticated:
                   login(request, user_object)
                   return HttpResponse('Login successful')
            return HttpResponse('invalid username and password')
    return render(request, 'signin.html', context)

