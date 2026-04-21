from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import account,map
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
        maps = map.objects.all()

        data = []
        for m in maps:
            data.append({
                "id": m.id_map,
                "name": m.name,
                "created_at": m.created_at,
            })

        return JsonResponse({"maps": data})

    return JsonResponse({"error": "Méthode non autorisée"}, status=405)