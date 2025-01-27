"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("helloworld.urls")),
    path('', include("crud_app.urls")),
    path('', include("registration.urls")),
    path('', include("Restframework_crudapp.urls")),
    path('', include("Restframe_Registration.urls")),
    path('', include("image.urls")),
    path('', include("image_binary.urls")),
    path('', include("Session_Registration.urls")),
    path('', include("image_folder.urls")),
    path('', include("ORM.urls")),
    path('', include("Multilevel_session.urls")),
    path('', include("Oauth.urls")),
    path('', include("Logging.urls")),
    path('', include("Encryption.urls")),
    path('', include("Currency.urls")),
    path('', include("Password_Validation.urls")),
    path('', include("AGE.urls")),
    path('', include("DOB.urls")),
    path('', include("Age_Difference.urls")),
    path('', include("QR_Code.urls")),
    path('', include("Bar_Code.urls")),
    path('', include("decimal_precision.urls")),
    path('', include("Time_Zone.urls")),
    path('', include("Time_stamp.urls")),
    path('', include("BMI.urls")),
    path('', include("Num2Word.urls")),
    path('', include("File_Path.urls")),
    path('', include("Forget_RestPassword.urls")),
]
