from django.urls import path
from.views import change

urlpatterns = [
    path('binary', change),

]
