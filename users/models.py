from django.db import models

# Create your models here.
from enum_field import Enum, EnumField

GENDER_CHOICES = Enum(
    ('M', 'Male'),
    ('F', 'Female'),
)


class SceneUser(models.Model):
    name = models.CharField(max_length=50, blank=None, null=None)
    age = models.PositiveSmallIntegerField()
    gender = EnumField(GENDER_CHOICES)






