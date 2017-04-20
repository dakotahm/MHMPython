from django.db import models

# Create your models here.
class Entries(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent = models.BigIntegerField()
    data = models.CharField(max_length=20000)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entries'


class Measurables(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=32)
    max = models.IntegerField(blank=True, null=True)
    min = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'measurables'
