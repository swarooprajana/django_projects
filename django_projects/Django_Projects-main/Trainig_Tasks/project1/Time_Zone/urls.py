from django.urls import path
from .views import Register


urlpatterns = [
    path('zone', Register.as_view()),
]
