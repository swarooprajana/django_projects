from django.shortcuts import render
from .models import Binary
from django.http import HttpResponse
from .base64 import convert


def change(request):
    if request.method == "POST":
        g = Binary()
        k = request.POST.get('image')
        g.image = convert(k)
        print(g.image)
        g.save()
        return HttpResponse("success")
    return render(request, "convert.html")