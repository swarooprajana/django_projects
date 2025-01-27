from django.shortcuts import render
from .models import Hotel
from datetime import datetime
from django.http import HttpResponse


def upload(request):
    if request.method == 'POST':
        i = Hotel()
        i.name = request.POST.get("name")
        i.image = request.FILES("image")
        i.date = datetime.now()
        #print(i.image)
        i.save()
        return HttpResponse("successfull")
    else:
        return render(request, 'image.html')

