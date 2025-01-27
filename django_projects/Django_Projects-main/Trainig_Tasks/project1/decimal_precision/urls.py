from django.urls import path
from .views import Register

urlpatterns = [
    path('decimal', Register.as_view())
]
