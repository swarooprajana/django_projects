from django.urls import path
from.views import *

urlpatterns = [
    path('o_register', Registration.as_view()),
    path('o_login', Login.as_view()),

]