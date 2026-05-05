from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
import json
import random

@csrf_exempt
def register(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({}, status=400)

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not name or not email or not password:
            return JsonResponse({}, status=400)

        if Account.objects.filter(email=email).exists():
            return JsonResponse({}, status=400)
        
        elif Account.objects.filter(name=name).exists():
            return JsonResponse({}, status=400) 

        code = str(random.randint(100000, 999999))

        Account.objects.create(
            name=name,
            email=email,
            password=make_password(password),
            verification_code=code
        )
        send_mail(
            "Code de vérification",
            f"Ton code est : {code}",
            "infectedPrison",
            [email],
            fail_silently=False,
        )

        return JsonResponse({},status=200)
    
    return JsonResponse({}, status=405)
    
@csrf_exempt
def verify_code(request):
    if request.method == "POST":
        data = json.loads(request.body)

        email = data.get("email")
        code = data.get("code")

        try:
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            return JsonResponse({}, status=404)

        if user.verification_code == code:
            user.is_verified = True
            user.verification_code = None
            user.save()

            return JsonResponse({},status=200)
        else:
            return JsonResponse({}, status=400)
        
    return JsonResponse({}, status=405)

@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        password = data.get("password")

        try:
            user = Account.objects.get(name=name)
        except Account.DoesNotExist:
            return JsonResponse({"error": "Utilisateur introuvable"}, status=404)

        if check_password(password, user.password):
            if not user.is_verified:
                return JsonResponse({"error": "Compte non vérifié"}, status=403)

            request.session['user_id'] = user.id_account
            request.session['user_name'] = user.name

            return JsonResponse({},status=200)
        else:
            return JsonResponse({}, status=400)

    return JsonResponse({}, status=405)

@csrf_exempt
def forget_password(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({}, status=400)
        
        email = data.get("email")
        if not email:
            return JsonResponse({})
        
        try:
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            return JsonResponse({}, status=404)
        
        code = str(random.randint(100000, 999999))
        user.verification_code = code
        user.save()

        send_mail(
            "Code de vérification",
            f"Ton code est : {code}",
            "infectedPrison",
            [email],
            fail_silently=False,
        )
        return JsonResponse({})

    return JsonResponse({}, status=405)

@csrf_exempt
def reset_password(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({}, status=400)
        
        email = data.get("email")
        password = data.get("password")

        if not password:
            return JsonResponse({})
        
        try:
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            return JsonResponse({}, status=404)
        
        user.password = make_password(password)
        user.save()

        return JsonResponse({})

    return JsonResponse({}, status=405)

def get_maps(request):
    if request.method == "GET":
        user_id = request.session.get('user_id')

        if not user_id:
            return JsonResponse({}, status=401)

        maps = Map.objects.filter(id_map__in=Save.objects.filter(player__id_account=user_id).values_list('id_map', flat=True)).distinct()
        data = []
        for map in maps:
            data.append({
                "id": map.id_map,
                "name": map.name,
                "created_at": map.created_at,
            })

        return JsonResponse({"maps": data})

    return JsonResponse({}, status=405)

def get_saves(request):
    if request.method == "GET":
        user_id = request.session.get('user_id')

        if not user_id:
            return JsonResponse({}, status=401)

        saves = Save.objects.filter(player__id_account=user_id).distinct()

        data = []

        for save_item in saves:
            players_data = []

            for player in save_item.player_set.all():
                players_data.append({
                    "id_player": player.id_player,
                    "health": player.health,
                    "energy": player.energy,
                    "pos_x": player.pos_x,
                    "pos_y": player.pos_y,
                    "created_at": player.created_at,
                    "name": player.name,
                    "is_owner": player.is_owner
                })

            data.append({
                "id_save": save_item.id_save,
                "created_at": save_item.created_at,
                "updated_at": save_item.updated_at,
                "duration": save_item.duration,
                "id_map": save_item.id_map.id_map,
                "is_win": save_item.is_win,
                "is_failed": save_item.is_failed,
                "players": players_data
            })

        return JsonResponse(data, safe=False)

    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

def get_info(request):
    if request.method == "GET":
        user_id = request.session.get('user_id')

        if not user_id:
            return JsonResponse({}, status=401)
        
    try:
        user = Account.objects.get(id_account=user_id)
    except Account.DoesNotExist:
        return JsonResponse({}, status=404)

    return JsonResponse({
        "id": user.id_account,
        "name": user.name,
        "email": user.email,
        "created_at": user.created_at,
        "is_verified":user.is_verified
    })

@csrf_exempt
def logout(request):
    if request.method == "POST":
        request.session.flush()  

        return JsonResponse({},status=200)

    return JsonResponse({}, status=405)

def get_save(request, id_save):
    if request.method != "GET":
        return JsonResponse({}, status=405)

    try:
        user_id = request.session.get('user_id')

        if not user_id:
            return JsonResponse({}, status=401)
        
        save_obj = Save.objects.get(id_save=id_save)

    except Save.DoesNotExist:
        return JsonResponse({}, status=404)

    players_data = []

    players = Player.objects.filter(id_save=save_obj)

    for player in players:
        
        items = ItemPossessed.objects.filter(id_player=player)

        items_data = []
        for item in items:
            item_obj = item.id_item

            items_data.append({
                "id_item_possessed": item.id_item_possessed,
                "created_at": item.created_at,
                "id_item": item_obj.id_item,
                "value": float(item_obj.value) if item_obj.value else None,
                "name": item_obj.name,
                "id_item_type": item_obj.id_item_type_id
            })

        players_data.append({
            "id_player": player.id_player,
            "health": player.health,
            "energy": player.energy,
            "pos_x": player.pos_x,
            "pos_y": player.pos_y,
            "created_at": player.created_at,
            "name": player.name,
            "is_owner": player.is_owner,
            "items": items_data
        })

    secret_items = ItemSecretPossessed.objects.filter(id_save=save_obj)

    secret_data = []
    for secret in secret_items:
        item_obj = secret.id_item

        secret_data.append({
            "id_item_secret_possessed": secret.id_item_secret_possessed,
            "created_at": secret.created_at,
            "id_item": item_obj.id_item,
            "value": float(item_obj.value) if item_obj.value else None,
            "name": item_obj.name,
            "id_item_type": item_obj.id_item_type_id
        })

    finish_data = []
    finishes = ToFinish.objects.filter(id_save=save_obj)

    for finish in finishes:
        finish_data.append({
            "id_save": finish.id_save_id,
            "id_puzzle": finish.id_puzzle_id,
            "created_at": finish.created_at
        })

    puzzles = Puzzle.objects.all()

    puzzles_data = []
    for puzzle in puzzles:
        puzzles_data.append({
            "id_puzzle": puzzle.id_puzzle,
            "title": puzzle.title,
            "content": puzzle.content,
            "item": None  
        })

    
    open_data = []
    opens = ToOpen.objects.filter(id_save=save_obj)

    for open in opens:
        open_data.append({
            "id_save": open.id_save_id,
            "id_sprite": open.id_sprite_id,
            "created_at": open.created_at
        })

    sprite_doors_data = []
    doors = SpriteDoor.objects.filter(id_map=save_obj.id_map)

    for door in doors:
        sprite_obj = door.id_sprite

        sprite_doors_data.append({
            "id_sprite": sprite_obj.id_sprite,
            "id_sprite_door_type": door.id_sprite_door_type_id,
            "pos_x": sprite_obj.pos_x,
            "pos_y": sprite_obj.pos_y,
            "image": sprite_obj.image
        })

    sprite_items_data = []
    sprite_items = SpriteItem.objects.all()

    for sprite_item in sprite_items:
        sprite_obj = sprite_item.id_sprite
        item_obj = sprite_item.id_item

        sprite_items_data.append({
            "id_sprite": sprite_obj.id_sprite,
            "pos_x": sprite_obj.pos_x,
            "pos_y": sprite_obj.pos_y,
            "image": sprite_obj.image,
            "created_at": sprite_item.created_at,
            "id_item": item_obj.id_item,
            "value": float(item_obj.value) if item_obj.value else None,
            "name": item_obj.name,
            "id_item_type": item_obj.id_item_type_id
        })

    enemies_data = []
    enemies = SpriteEnemy.objects.all()

    for enemy in enemies:
        sprite_obj = enemy.id_sprite

        enemies_data.append({
            "id_sprite": sprite_obj.id_sprite,
            "pos_x": sprite_obj.pos_x,
            "pos_y": sprite_obj.pos_y,
            "image": sprite_obj.image,
            "created_at": enemy.created_at,
            "health": enemy.health,
            "damage": enemy.damage
        })

    return JsonResponse({
        "id_save": save_obj.id_save,
        "created_at": save_obj.created_at,
        "updated_at": save_obj.updated_at,
        "duration": save_obj.duration,
        "id_map": save_obj.id_map_id,
        "is_win": save_obj.is_win,
        "is_failed": save_obj.is_failed,
        "players": players_data,
        "items_secret": secret_data,
        "finish": finish_data,
        "puzzles": puzzles_data,
        "open": open_data,
        "sprite_doors": sprite_doors_data,
        "sprite_items": sprite_items_data,
        "sprite_enemies": enemies_data
    })

@csrf_exempt
def save_player(request):
    if request.method != "POST":
        return JsonResponse({}, status=405)

    try:
        user_id = request.session.get('user_id')

        if not user_id:
            return JsonResponse({}, status=401)

        body = json.loads(request.body)

        id_player = body.get("id_player")
        health = body.get("health")
        energy = body.get("energy")
        pos_x = body.get("pos_x")
        pos_y = body.get("pos_y")

        if not id_player:
            return JsonResponse({}, status=400)

        player = Player.objects.get(id_player=id_player)

        if player.id_account_id != user_id:
            return JsonResponse({}, status=403)

        player.health = health
        player.energy = energy
        player.pos_x = pos_x
        player.pos_y = pos_y
        player.save()

        return JsonResponse({})

    except Player.DoesNotExist:
        return JsonResponse({}, status=404)

    except Exception as e:
        return JsonResponse({}, status=500)
    

@csrf_exempt
def finish_puzzle(request):
    if request.method != "POST":
        return JsonResponse({}, status=405)

    try:
        user_id = request.session.get('user_id')

        if not user_id:
            return JsonResponse({}, status=401)

        body = json.loads(request.body)

        id_save = body.get("id_save")
        id_puzzle = body.get("id_puzzle")

        if not id_save or not id_puzzle:
            return JsonResponse({}, status=400)

        save_obj = Save.objects.get(id_save=id_save)
        puzzle = Puzzle.objects.get(id_puzzle=id_puzzle)

        if not Player.objects.filter(id_save=save_obj, id_account_id=user_id).exists():
            return JsonResponse({}, status=403)

        if ToFinish.objects.filter(id_save=save_obj, id_puzzle=puzzle).exists():
            return JsonResponse({""}, status=400)

        ToFinish.objects.create(
            id_save=save_obj,
            id_puzzle=puzzle,
            created_at=now()
        )

        reward_item = Item.objects.first()

        players = Player.objects.filter(id_save=save_obj)

        for player in players:
            ItemPossessed.objects.create(
                id_player=player,
                id_item=reward_item
            )

        return JsonResponse({})

    except Save.DoesNotExist:
        return JsonResponse({}, status=404)

    except Puzzle.DoesNotExist:
        return JsonResponse({}, status=404)

    except Exception as e:
        return JsonResponse({}, status=500)   

@csrf_exempt
def open_door(request):
    if request.method != "POST":
        return JsonResponse({}, status=405)

    try:
        body = json.loads(request.body)

        id_save = body.get("id_save")
        id_sprite = body.get("id_sprite")

        if not id_save or not id_sprite:
            return JsonResponse({}, status=400)

        save_obj = Save.objects.get(id_save=id_save)
        door = SpriteDoor.objects.get(id_sprite=id_sprite)

        # 🔒 déjà ouverte ?
        if ToOpen.objects.filter(id_save=save_obj, id_sprite=door).exists():
            return JsonResponse({}, status=400)

        door_type = door.id_sprite_door_type.id_sprite_door_type

        players = Player.objects.filter(id_save=save_obj)

        if door_type == "KEY":

            key_removed = False

            for player in players:
                key_item = ItemPossessed.objects.filter(
                    id_player=player,
                    id_item__id_item_type__id="KEY"
                ).first()

                if key_item:
                    key_item.delete()  
                    key_removed = True
                    break

            if not key_removed:
                return JsonResponse({}, status=400)

        ToOpen.objects.create(
            id_save=save_obj,
            id_sprite=door,
            created_at=now()
        )

        return JsonResponse({},status=200)

    except Save.DoesNotExist:
        return JsonResponse({}, status=404)

    except SpriteDoor.DoesNotExist:
        return JsonResponse({}, status=404)

    except Exception as e:
        return JsonResponse({}, status=500) 