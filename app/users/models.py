from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    my_referal_code = models.CharField(max_length=250, null=True, blank=True)
    referal_points = models.PositiveBigIntegerField(default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def generate_referal_code(self):
        if not self.my_referal_code:
            self.my_referal_code = f"RFRC{self.pk}"
