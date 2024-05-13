from django.contrib import admin
from django.urls import path
from testProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signinPage/',signinPage,name="signinPage"),
    path('signupPage/',signupPage,name="signupPage"),
]
