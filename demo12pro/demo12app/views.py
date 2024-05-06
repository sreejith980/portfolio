from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def hello(request):
    if request.method == 'POST':
        name = request.POST['name']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        yourmessage = request.POST['yourmessage']
        login(name=name, phonenumber=phonenumber, email=email, yourmessage=yourmessage).save()
        return redirect('bye')
    return render(request, 'hello.html')
def bye(request):
    return render(request, 'bye.html')