from django.urls import path
from .views import Register

urlpatterns = [
    path('bmi', Register.as_view()),
]
