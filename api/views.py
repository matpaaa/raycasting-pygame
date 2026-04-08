from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import account
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
