from django.urls import path
from .views import Register, Login

urlpatterns = [
    path('ency_reg', Register.as_view()),
    path('ency_log', Login.as_view()),
]
