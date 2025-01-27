from django.urls import path
from .views import Register


urlpatterns = [
    path('diff', Register.as_view()),
]
