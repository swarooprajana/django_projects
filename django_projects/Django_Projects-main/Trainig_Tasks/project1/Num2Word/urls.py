from django.urls import path
from .views import Register

urlpatterns = [
    path('word', Register.as_view()),
]
