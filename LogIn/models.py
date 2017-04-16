from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=64)
    password = models.CharField(max_length=64)
    last_ip = models.CharField(max_length=64, blank=True, null=True)
    last_access = models.DateTimeField(blank=True, null=True)
    session_token = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username;

    class Meta:
        managed = False
        db_table = 'users'
