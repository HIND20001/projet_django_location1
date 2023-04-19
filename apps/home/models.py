# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.db import models


class vehicule(models.Model):
    matricule = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    marqueV = models.CharField(max_length=100, blank=True)
    model = models.CharField(max_length=100)
    puissance = models.IntegerField()
    nbr_place = models.IntegerField()
    auto_menu = models.CharField(max_length=100)
    prix = models.FloatField()
    photo = models.CharField(max_length=100)


class reservation(models.Model):
    client = models.CharField(max_length=100)
    matricule = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField()
    prix = models.FloatField()
# Create your models here.
