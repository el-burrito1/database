# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import csv

# Create your models here

class Player(models.Model):
	year = models.CharField(max_length=5)
	height = models.IntegerField()
	hometown = models.CharField(max_length=50)
	name = models.CharField(max_length=30)
	position = models.CharField(max_length=5)
	weight = models.IntegerField()


class Player_lite(models.Model):
	name = models.CharField(max_length=50)
	number = models.IntegerField()





