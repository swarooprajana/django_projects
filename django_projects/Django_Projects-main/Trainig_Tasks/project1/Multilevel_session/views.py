from django.shortcuts import render
from .models import Session
from django.shortcuts import HttpResponse


def register(request):
    if request.method == "POST":
        k = Session()
        k.username = request.POST.get("username")
        k.password = request.POST.get("password")
        k.email = request.POST.get("email")
        k.address = request.POST.get("address")
        k.save()
        return HttpResponse("successful")
    else:
        return render(request, "Register.html")


def login1(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        n = Session.objects.get(username=username)
        print(n)
        request.session["name"] = n.username
        request.session.set_expiry(10)
        if password == n.password:
            return HttpResponse("successfull")
        else:
            return HttpResponse("please check the details")
    return render(request, "set.html")

def getsession1(request):
    if 'name' in request.session:
        name = request.session['name']
        return render(request, 'get_session.html', {'name': name})
    else:
        return HttpResponse("your session was expired....")





def login2(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        n = Session.objects.get(username=username)
        print(n)
        request.session["name"] = n.username
        request.session.set_expiry(20)
        if password == n.password:
            return HttpResponse("successfull")
        else:
            return HttpResponse("please check the details")
    return render(request, "set.html")

def getsession2(request):
    if 'name' in request.session:
        name = request.session['name']
        return render(request, 'get_session.html', {'name': name})
    else:
        return HttpResponse("your session was expired......")




def login3(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        n = Session.objects.get(username=username)
        print(n)
        request.session["name"] = n.username
        request.session.set_expiry(30)
        if password == n.password:
            return HttpResponse("successfull")
        else:
            return HttpResponse("please check the details")
    return render(request, "set.html")

def getsession3(request):
     if 'name' in request.session:
         name = request.session['name']
         return render(request, 'get_session.html', {'name': name})
     else:
         return HttpResponse("your session was expired..........")


