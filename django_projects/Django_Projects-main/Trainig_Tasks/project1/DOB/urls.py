from django.urls import path
from .views import Register

urlpatterns = [
    path('dob', Register.as_view())
]