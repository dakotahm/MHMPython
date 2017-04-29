
from __future__ import unicode_literals

from django.db import models



class Entries(models.Model):
    """ORM for data entries"""
    id = models.BigAutoField(primary_key=True)
    parent = models.BigIntegerField()
    data = models.CharField(max_length=20000)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entries'


class Measurables(models.Model):
    """ORM for data Measurables"""
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=32)
    max = models.IntegerField(blank=True, null=True)
    min = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'measurables'


class Users(models.Model):
    """ORM for data users"""
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=64)
    password = models.CharField(max_length=64)
    last_ip = models.CharField(max_length=64, blank=True, null=True)
    last_access = models.DateTimeField(blank=True, null=True)
    session_token = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

class TreatmentDownloads(models.Model):
    """ORM for data Downloadable files"""
    id = models.AutoField(primary_key=True)
    Filename = models.CharField( max_length=100)
    Description = models.CharField(max_length=250)
    URL = models.CharField(max_length=250,  null=True)
    Global = models.SmallIntegerField(null=True)
    UserFK=models.IntegerField()

    class Meta:
        managed = False
        db_table = 'TreatmentDownloads'
