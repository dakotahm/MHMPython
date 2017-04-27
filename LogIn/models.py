from django.db import models


class AuthUser(models.Model):
    """
    AuthUser model is used for all users. Stored in a table in MySQL database
    
    """
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    def __str__(self):
        """
        Method for reading this model's username attribute
        
        :return: 
        """
        return self.username;

    class Meta:
        """
        Associated with auth_user table in MySQL database
        
        """
        managed = False
        db_table = 'auth_user'
