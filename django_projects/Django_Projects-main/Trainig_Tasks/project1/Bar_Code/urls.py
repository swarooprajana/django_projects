from django.urls import path
from .views import Register


urlpatterns = [
    path('barcode', Register.as_view()),
]
