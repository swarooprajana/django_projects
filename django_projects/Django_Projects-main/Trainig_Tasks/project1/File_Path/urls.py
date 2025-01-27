from .views import upload
from django.urls import path


urlpatterns = [
    path('file', upload),
]
