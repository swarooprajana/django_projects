from django.urls import path
from .views import Registration, login_user

urlpatterns = [
    path('register', Registration),
    path('login', login_user),
]
