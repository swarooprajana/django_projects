from django.urls import path
from .views import folder,read


urlpatterns = [
    path('fold', folder),
    path('gett', read),
]
