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
            return JsonResponse({"error": "JSON invalide"}, status=400)

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not name or not email or not password:
            return JsonResponse({"error": "Champs manquants"}, status=400)

        if account.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email déjà utilisé"}, status=400)
        
        elif account.objects.filter(name=name).exists():
            return JsonResponse({"error": "Nom d'utilisateur déjà utilisé"}, status=400) 

        code = str(random.randint(100000, 999999))

        account.objects.create(
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

        return JsonResponse({"message": "Code envoyé"})
    
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)
    
@csrf_exempt
def verify_code(request):
    if request.method == "POST":
        data = json.loads(request.body)

        email = data.get("email")
        code = data.get("code")

        try:
            user = account.objects.get(email=email)
        except account.DoesNotExist:
            return JsonResponse({"error": "Utilisateur introuvable"}, status=404)

        if user.verification_code == code:
            user.is_verified = True
            user.verification_code = None
            user.save()

            return JsonResponse({"message": "Compte vérifié ✅"})
        else:
            return JsonResponse({"error": "Code incorrect"}, status=400)
        
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        password = data.get("password")

        try:
            user = account.objects.get(name=name)
        except account.DoesNotExist:
            return JsonResponse({"error": "Utilisateur introuvable"}, status=404)

        if check_password(password, user.password):
            if not user.is_verified:
                return JsonResponse({"error": "Compte non vérifié"}, status=403)

            request.session['user_id'] = user.id_account
            request.session['user_name'] = user.name

            return JsonResponse({"message": "Connecté ✅"})
        else:
            return JsonResponse({"error": "Mot de passe incorrect"}, status=400)

    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

@csrf_exempt
def forget_password(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"error": "JSON invalide"}, status=400)
        
        email = data.get("email")
        if not email:
            return JsonResponse({"error": "Champ manquant"})
        
        try:
            user = account.objects.get(email=email)
        except account.DoesNotExist:
            return JsonResponse({"error": "Utilisateur introuvable"}, status=404)
        
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
        return JsonResponse({"message": "code envoyer"})

    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

@csrf_exempt
def reset_password(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"error": "JSON invalide"}, status=400)
        
        email = data.get("email")
        password = data.get("password")

        if not password:
            return JsonResponse({"error": "Champ manquant"})
        
        try:
            user = account.objects.get(email=email)
        except account.DoesNotExist:
            return JsonResponse({"error": "Utilisateur introuvable"}, status=404)
        
        user.password = make_password(password)
        user.save()

        return JsonResponse({"message": "Mots de passe changer"})

    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

def get_maps(request):
    if request.method == "GET":
        user_id = request.session.get('user_id')

        if not user_id:
            return JsonResponse({"error": "Non connecté"}, status=401)

        maps = map.objects.filter(id_map__in=save.objects.filter(player__id_account=user_id).values_list('id_map', flat=True)).distinct()
        data = []
        for m in maps:
            data.append({
                "id": m.id_map,
                "name": m.name,
                "created_at": m.created_at,
            })

        return JsonResponse({"maps": data})

    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

def get_saves(request):
    if request.method == "GET":
        user_id = request.session.get('user_id')

        if not user_id:
            return JsonResponse({"error": "Non connecté"}, status=401)

        saves = save.objects.filter(player__id_account=user_id).distinct()

        data = []

        for save_item in saves:
            players_data = []

            for p in save_item.player_set.all():
                players_data.append({
                    "id_player": p.id_player,
                    "health": p.health,
                    "energy": p.energy,
                    "pos_x": float(p.pos_x),
                    "pos_y": float(p.pos_y),
                    "created_at": p.created_at,
                    "name": p.name,
                    "is_owner": p.is_owner
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
            return JsonResponse({"error": "Non connecté"}, status=401)
        
    try:
        user = account.objects.get(id_account=user_id)
    except account.DoesNotExist:
        return JsonResponse({"error": "Utilisateur introuvable"}, status=404)

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

    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

def get_save(request, id_save):
    if request.method != "GET":
        return JsonResponse({"error": "Méthode non autorisée"}, status=405)

    try:
        save_obj = save.objects.get(id_save=id_save)
    except save.DoesNotExist:
        return JsonResponse({"error": "Save introuvable"}, status=404)

    players_data = []

    players = player.objects.filter(id_save=save_obj)

    for p in players:
        
        items = ItemPossessed.objects.filter(id_player=p)

        items_data = []
        for it in items:
            item_obj = it.id_item

            items_data.append({
                "id_item_possessed": it.id_item_possessed,
                "created_at": it.created_at,
                "id_item": item_obj.id_item,
                "value": float(item_obj.value) if item_obj.value else None,
                "name": item_obj.name,
                "id_item_type": item_obj.id_item_type.id_item_type
            })

        players_data.append({
            "id_player": p.id_player,
            "health": p.health,
            "energy": p.energy,
            "pos_x": float(p.pos_x),
            "pos_y": float(p.pos_y),
            "created_at": p.created_at,
            "name": p.name,
            "is_owner": p.is_owner,
            "items": items_data
        })

    secret_items = item_secret_possessed.objects.filter(id_save=save_obj)

    secret_data = []
    for s in secret_items:
        item_obj = s.id_item

        secret_data.append({
            "id_item_secret_possessed": s.id_item_secret_possessed,
            "created_at": s.created_at,
            "id_item": item_obj.id_item,
            "value": float(item_obj.value) if item_obj.value else None,
            "name": item_obj.name,
            "id_item_type": item_obj.id_item_type.id_item_type
        })

    finish_data = []
    finishes = to_finish.objects.filter(id_save=save_obj)

    for f in finishes:
        finish_data.append({
            "id_save": f.id_save.id_save,
            "id_puzzle": f.id_puzzle.id_puzzle,
            "created_at": f.created_at
        })

    puzzles = puzzle.objects.all()

    puzzles_data = []
    for puz in puzzles:
        puzzles_data.append({
            "id_puzzle": puz.id_puzzle,
            "title": puz.title,
            "content": puz.content,
            "item": None  
        })

    
    open_data = []
    opens = to_open.objects.filter(id_save=save_obj)

    for o in opens:
        open_data.append({
            "id_save": o.id_save.id_save,
            "id_sprite": o.id_sprite.id_sprite,
            "created_at": o.created_at
        })

    sprite_doors_data = []
    doors = sprite_door.objects.filter(id_map=save_obj.id_map)

    for d in doors:
        sprite_obj = d.id_sprite

        sprite_doors_data.append({
            "id_sprite": sprite_obj.id_sprite,
            "id_sprite_door_type": d.id_sprite_door_type.id_sprite_door_type,
            "pos_x": float(sprite_obj.pos_x),
            "pos_y": float(sprite_obj.pos_y),
            "image": sprite_obj.image
        })

    sprite_items_data = []
    sprite_items = sprite_item.objects.all()

    for si in sprite_items:
        sprite_obj = si.id_sprite
        item_obj = si.id_item

        sprite_items_data.append({
            "id_sprite": sprite_obj.id_sprite,
            "pos_x": float(sprite_obj.pos_x),
            "pos_y": float(sprite_obj.pos_y),
            "image": sprite_obj.image,
            "created_at": si.created_at,
            "id_item": item_obj.id_item,
            "value": float(item_obj.value) if item_obj.value else None,
            "name": item_obj.name,
            "id_item_type": item_obj.id_item_type.id_item_type
        })

    enemies_data = []
    enemies = sprite_enemy.objects.all()

    for e in enemies:
        sprite_obj = e.id_sprite

        enemies_data.append({
            "id_sprite": sprite_obj.id_sprite,
            "pos_x": float(sprite_obj.pos_x),
            "pos_y": float(sprite_obj.pos_y),
            "image": sprite_obj.image,
            "created_at": e.created_at,
            "health": e.health,
            "damage": e.damage
        })

    return JsonResponse({
        "id_save": save_obj.id_save,
        "created_at": save_obj.created_at,
        "updated_at": save_obj.updated_at,
        "duration": save_obj.duration,
        "id_map": save_obj.id_map.id_map,
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