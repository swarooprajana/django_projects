from django.http import HttpResponse
from django.shortcuts import render
from.models import image


def folder(request):
    if request.method == "POST":
        f = image()
        f.image = request.FILES["image"]
        print(f.image)
        f.save()
        return HttpResponse("successfull")
    else:
        return render(request, "folder.html")

def read(request):
    get_image = image.objects.all()
    return render(request, "get.html", {"image": get_image })






