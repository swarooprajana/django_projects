from django.shortcuts import render, redirect
from.models import RegistrationModel
from django.http import HttpResponse


def Create(request):
    if request.method == "POST":
        v = RegistrationModel()
        v.name = request.POST.get('name')
        v.email = request.POST.get('email')
        v.phone = request.POST.get('phone')
        v.address = request.POST.get('address')
        v.save()
        return HttpResponse("success")
    else:
        return render(request, 'create.html')


def Read(request):
    var = RegistrationModel.objects.all()
    return render(request, 'read.html', {'RegistrationModel': var})


def Update(request, id):
    if request.method == 'POST':
        v = RegistrationModel.objects.get(id=id)
        v.name = request.POST.get('name')
        v.email = request.POST.get('email')
        v.phone = request.POST.get('phone')
        v.address = request.POST.get('address')
        v.save()
        return HttpResponse('updated')
    else:
        return render(request, 'update.html')


def Delete(request, id):
    x = RegistrationModel.objects.get(id=id)
    x.delete()
    return redirect(Read)
