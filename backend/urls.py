from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register', register),
    path('api/login', login),
    path('api/verify-code', verify_code),
    path('api/forgot-password', forget_password),
    path('api/reset-password', reset_password),
    path('api/maps', get_maps),
    path('api/saves', get_saves),
    path('api/me', get_info),
    path('api/logout', logout),
    path('api/player/save', save_player),
    path('api/puzzle/finish', finish_puzzle),
    path('api/recover/item', recover_item),
    path('api/drop/item', drop_item),
    path('api/door/open', open_door),
    path('api/delete/save', delete_save),
    path('api/create/save', create_save),
    path('api/auth/status', auth_status),
    path('api/delete/account', delete_account),
    path('api/save/online', save_online),
    path('api/save/win', win),
    path('api/save/failed', failed),
    path('api/save/join', join_save),
    path('api/save/consumable', consumable),
    path('api/save/shoot', shoot_enemy),
    path('api/save/<id_save>', get_save),
]
