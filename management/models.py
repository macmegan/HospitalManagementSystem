from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.username
    
class Room(models.Model):
    class Department(models.TextChoices):
        RADIOLOGY = 'Radiology'
        PSYCHIATRY = 'Psychiatry'
        SURGERY = 'Surgery'
        PAEDIATRICS = 'Paediatrics'
        ONCOLOGY = 'Oncology'
        NURSING = 'Nursing'


    department = models.CharField(
        max_length=11,
        choices=Department.choices, 
        default=Department.NURSING
    )

    capacity = models.IntegerField(default=20)
    
    imageNum = models.CharField(max_length=20, default='default')

class Reservation(models.Model):  
    user = models.ForeignKey('management.User', on_delete=models.CASCADE)
    room = models.ForeignKey('management.Room', on_delete=models.CASCADE)