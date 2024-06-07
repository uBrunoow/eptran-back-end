import uuid
import random
import string
from django.db import models
from utils.models import BaseModel
from cuser.models import AbstractCUser
from django.conf import settings


class BrazilianState(models.TextChoices):
    AC = "AC", "Acre"
    AL = "AL", "Alagoas"
    AP = "AP", "Amapá"
    AM = "AM", "Amazonas"
    BA = "BA", "Bahia"
    CE = "CE", "Ceará"
    ES = "ES", "Espírito Santo"
    GO = "GO", "Goiás"
    MA = "MA", "Maranhão"
    MT = "MT", "Mato Grosso"
    MS = "MS", "Mato Grosso do Sul"
    MG = "MG", "Minas Gerais"
    PA = "PA", "Pará"
    PB = "PB", "Paraíba"
    PR = "PR", "Paraná"
    PE = "PE", "Pernambuco"
    PI = "PI", "Piauí"
    RJ = "RJ", "Rio de Janeiro"
    RN = "RN", "Rio Grande do Norte"
    RS = "RS", "Rio Grande do Sul"
    RO = "RO", "Rondônia"
    RR = "RR", "Roraima"
    SC = "SC", "Santa Catarina"
    SP = "SP", "São Paulo"
    SE = "SE", "Sergipe"
    TO = "TO", "Tocantins"
    DF = "DF", "Distrito Federal"

class TransactionType(models.TextChoices):
    RENT = "RENT", "Rent"
    SALE = "SALE", "Sale"

class SexType(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"

class EducationType(models.TextChoices):
    ELEMENTARY1 = "ELEMENTARY1", "Elementary1"
    ELEMENTARY2 = "ELEMENTARY2", "Elementary2"
    ELEMENTARY4 = "ELEMENTARY3", "Elementary3"
    HIGHSCHOOL = "HIGHSCHOOL", "Highscool"

class PermissionsType(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    USER = "USER", "User"
    STAFF = "STAFF", "Staff"

class User(AbstractCUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=100, help_text="Nome do usuário", verbose_name="Nome"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, null=True, blank=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, editable=False, null=True, blank=True
    )


    class Meta(AbstractCUser.Meta):
        swappable = "AUTH_USER_MODEL"

    def save(self, **kwargs) -> None:
        return super().save(**kwargs)

    def __str__(self):
        return self.email + " | " + self.first_name + " " + self.last_name

class Admin(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin')
    permissions = models.CharField(max_length=50, choices=PermissionsType.choices, default=PermissionsType.ADMIN)

    def __str__(self):
        return f'Admin {self.id} of user {self.user.name}'

class Staff(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff')
    permissions = models.CharField(max_length=50, choices=PermissionsType.choices, default=PermissionsType.STAFF)

    def __str__(self):
        return f'Staff {self.id} of user {self.user.name}'

class Student(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    permissions = models.CharField(max_length=50, choices=PermissionsType.choices, default=PermissionsType.USER)

    def __str__(self):
        return f'Student {self.id} of user {self.user.name}'
    
class News(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    subtitle = models.TextField(null=False)
    first_paragraph = models.TextField(null=False)
    second_paragraph = models.TextField(null=True, blank=True)
    third_paragraph = models.TextField(null=True, blank=True)
    fourth_paragraph = models.TextField(null=True, blank=True)
    fifth_paragraph = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.title
    
class SavedNews(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return f'Saved news {self.news.title} by user {self.user.name}'
    
class Game(BaseModel):
    name = models.CharField(max_length=255, null=False)
    classification = models.CharField(
        max_length=50,
        choices=EducationType.choices,
        null=False
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