from django.urls import path
from.views import Registration,Login


urlpatterns = [
    path('registration', Registration.as_view()),
    path('Login', Login.as_view())
]