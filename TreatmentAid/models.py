from django.db import models

# Create your models here.
class Treatmentdownloads(models.Model):
    filename = models.CharField(db_column='Filename', max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=250)  # Field name made lowercase.
    global_field = models.IntegerField(db_column='Global')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    userfk = models.IntegerField(db_column='UserFK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table =
