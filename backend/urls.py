from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', register),
    path('api/login/', login),
    path('api/verify-code/', verify_code),
    path('api/forget-password/', forget_password),
    path('api/reset-password/', reset_password),
    path('api/get-maps/', get_maps),
    path('api/get-saves/', get_saves),
    path('api/get-info/', get_info),
]
