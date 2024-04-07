from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=100, unique=True)
    referal_code = models.CharField(max_length=250, null=True, blank=True)

    USERNAME_FIELD = "name"
    REQUIRED_FIELDS = ["email"]

    def generate_referal_code(self):
        if not self.referal_code:
            self.referal_code = f"RFRC{self.pk}"
            self.save()
