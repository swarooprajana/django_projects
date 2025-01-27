from django.shortcuts import render
from.models import UserRegistration
from django.http import HttpResponse


def Registration(request):
    if request.method == "POST":
        r = UserRegistration()
        r.username = request.POST.get('username')
        r.password = request.POST.get('password')
        r.firstname = request.POST.get('firstname')
        r.lastname = request.POST.get('lastname')
        r.email = request.POST.get('email')
        r.save()
        return HttpResponse("successfull")
    else:
        return render(request, 'Registration.html')


def login_user(request):
     if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        page = UserRegistration.objects.get(username=username)
        print(username)
        if page.password == password:
            return HttpResponse('success')
        else:
            return HttpResponse('check the details')
     return render(request, 'Login.html')


