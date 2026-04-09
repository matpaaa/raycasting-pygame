from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', register),
    path('api/login/', login),
    path('api/verifyCode/', verify_code),
    path('api/forgetPassword/', forget_password),
    path('api/resetPassword/', reset_password),
]
