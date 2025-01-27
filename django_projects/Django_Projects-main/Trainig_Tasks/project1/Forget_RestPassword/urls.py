from django.urls import path
from .views import Register, update, Login

urlpatterns = [
    path('forgetpwd', Register.as_view()),
    path('fupdate/<int:id>', update.as_view()),
    path('pswd', Login.as_view()),
]