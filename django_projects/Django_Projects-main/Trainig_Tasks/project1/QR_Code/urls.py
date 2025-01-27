from django.urls import path
from .views import Register, get

urlpatterns = [
    path('qrgen', Register.as_view()),
    path('qrget', get),
]