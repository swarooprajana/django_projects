from django.urls import path
from .views import Reg

urlpatterns = [
    path('valid', Reg.as_view()),
]



