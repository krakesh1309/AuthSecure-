from django.shortcuts import render, redirect
from .forms import RegisterForm 
from .Loginform import LoginForm
from .models import User
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = request.POST.get('confirm_password')  
            if password == confirm_password:
                form.save()
                return redirect("login")
            else:
                return HttpResponse("Passwords do not match. Please try again.")
        else:
            return render(request, 'register.html', {'form': form})

    form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# create login functions
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username, password= password).first()
            if user:
                return HttpResponse("Login Successful !! Welcome, {}".format(user.fname))
            else:
                return HttpResponse("Invalid username and password. Please try again.")
        else:
            return render(request, 'login.html', {'form':form})
    form = LoginForm()
    return render(request, 'login.html', {'form':form})