from django.urls import path
from .views import Reg


urlpatterns = [
    path('currency', Reg.as_view()),
]
