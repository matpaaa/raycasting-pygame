from django.db import models
from django.utils.timezone import now

# Create your models here.
class account(models.Model):
    id_account = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=128)
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, null=True, blank=True)
    created_at = models.DateTimeField(default=now)
    email = models.EmailField(unique=True)