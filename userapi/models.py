from django.db import models


# Create your models here.
class Apiuser(models.Model):
    email=models.EmailField(max_length=254 , unique=True)
    first_name=models.CharField( max_length=150)
    last_name=models.CharField( max_length=150)
    avatar=models.CharField( max_length=150)
    date=models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.first_name
    