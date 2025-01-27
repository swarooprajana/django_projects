from django.urls import path
from .views import *


urlpatterns = [
    path('m_register', register),
    path('m_login1', login1),
    path('m_get1', getsession1),
    path('m_login2', login2),
    path('m_get2', getsession2),
    path('m_login3', login3),
    path('m_get3', getsession3),

]
