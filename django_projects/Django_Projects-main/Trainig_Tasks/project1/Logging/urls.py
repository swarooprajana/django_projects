from django.urls import path
from.views import log


urlpatterns = [
    path('logging', log.as_view()),

]