from django.urls import path
from .views import Register


urlpatterns = [
    path('age', Register.as_view()),
]