from django.shortcuts import render
from .models import file_models
from datetime import datetime
from django.http import HttpResponse


def upload(request):
    if request.method == "POST":
        f = file_models()
        f.name = request.POST.get("name")
        f.image = request.FILES["image"]
        f.dt = datetime.now()
        f.save()
        return HttpResponse("success")
    else:
        return render(request, 'file.html')
