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