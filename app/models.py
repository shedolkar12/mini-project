from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Soldiers(models.Model):
    name = models.CharField(max_length = 50)
    exp = models.IntegerField(max_length = 50)
    strength = models.CharField(max_length = 50)
    join_date = models.CharField(max_length = 50, default = '')
    def __str__(self):
        return u'%s' % (self.name)

class Weapons(models.Model):
    weapon = models.CharField(max_length = 50)
    quantity = models.IntegerField()
    available = models.CharField(max_length = 50)
    def __str__(self):
        return u'%s' % (self.weapon)

class Food(models.Model):
    food = models.CharField(max_length = 50)
    storage = models.IntegerField()
    expire = models.CharField(max_length = 50, default = '')

    def __str__(self):
        return u'%s' % (self.food)
        
