from django.urls import path
from .views import *
urlpatterns = [
    path('college', create.as_view()),
    path('room', file.as_view()),
    path('student', dairy.as_view()),
    #path('get@/<int:id>', Getdetail.as_view()),
    path('getcollege/<int:College>/', colllegeget.as_view()),

]