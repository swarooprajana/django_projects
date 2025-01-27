from django.urls import path
from .views import Create, Read, Update, Delete

urlpatterns = [
    path('post', Create),
    path('get', Read),
    path('update/<int:id>', Update),
    path('delete/<int:id>', Delete),
]






