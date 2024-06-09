import uuid
import random
import string
from django.db import models
from utils.models import BaseModel
from apps.management.models import User

class SexType(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"

class EducationType(models.TextChoices):
    ELEMENTARY1 = "ELEMENTARY1", "Elementary1"
    ELEMENTARY2 = "ELEMENTARY2", "Elementary2"
    ELEMENTARY4 = "ELEMENTARY3", "Elementary3"
    HIGHSCHOOL = "HIGHSCHOOL", "Highscool"

class EducationType(models.TextChoices):
    ELEMENTARY1 = "ELEMENTARY1", "Elementary1"
    ELEMENTARY2 = "ELEMENTARY2", "Elementary2"
    ELEMENTARY4 = "ELEMENTARY3", "Elementary3"
    HIGHSCHOOL = "HIGHSCHOOL", "Highscool"

class PermissionsType(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    USER = "USER", "User"
    STAFF = "STAFF", "Staff"

class Game(BaseModel):
    name = models.CharField(max_length=255, null=False)
    classification = models.CharField(
        max_length=50,
        choices=EducationType.choices,
        null=False
    )
    link = models.CharField(max_length=255, null=False, default="")
    description = models.TextField(null=False, default="")
    image = models.ImageField(
        upload_to="games/game/image",
        help_text="Imagem Capa do Jogo",
        verbose_name="Capa",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

class GameStatistics(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    time_spent = models.DurationField(null=True, blank=True)
    progress = models.IntegerField(null=True, blank=True)
    fastest_time = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f'Statistics for {self.game.name} by user {self.user.name if self.user else "Anonymous"}'