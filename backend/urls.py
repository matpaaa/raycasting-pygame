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
    path('api/logout/', logout),
    path('api/get-save/<id_save>/', get_save),
    path('api/player/save/', save_player),
    path('api/puzzle/finish/', finish_puzzle),
    path('api/recover/item/', recover_item),
    path('api/door/open/', open_door),
]
