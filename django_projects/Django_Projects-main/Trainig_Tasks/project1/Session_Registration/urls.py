from django. urls import path
from.views import registration,login,getsession

urlpatterns = [
    path("session", getsession),
    path('s_register', registration),
    path('s_login', login),

]