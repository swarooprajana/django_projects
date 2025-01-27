from django.shortcuts import render,HttpResponse,redirect
from .models import Registration


def getsession(request):
    if 'name' in request.session:
        name = request.session['name']
        return render(request, 'getsession.html', {'name': name})
    else:
        return HttpResponse("your session was expired")


def registration(request):
    if request.method == "POST":
        s = Registration()
        s.username = request.POST.get("username")
        s.password = request.POST.get("password")
        s.name = request.POST.get("name")
        s.email = request.POST.get("email")
        s.phone = request.POST.get("phone")
        s.save()
        request.session = ['name']
        return HttpResponse("successfull")
    else:
        return render(request,"Registration.html")

def login(request):
   if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      k = Registration.objects.get(username=username)
      print(k)
      request.session['name'] = k.username
      if password == k.password:
        return HttpResponse("successfull")
      else:
         return HttpResponse("check the details")
   return render(request, "Login.html")


