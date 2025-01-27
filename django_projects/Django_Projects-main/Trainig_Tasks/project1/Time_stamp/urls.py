from django.urls import path
from .views import Register


urlpatterns = [
    path('stamp', Register.as_view()),
]
