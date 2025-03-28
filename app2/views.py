from django.shortcuts import render
from .forms import Registration
from django.http import HttpResponse

# Create your views here.
def signupview(request):
    context = {
        'forms':Registration()
    }
    if request.method == 'POST':
        fm = Registration(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponse("Registrations Successful")
    return render(request, 'signup.html', context)

