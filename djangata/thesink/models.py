from django.db import models

# Create your models here.
class Title(models.Model):
    name = models.CharField(max_length=32)
    data = models.CharField(max_length=200)
    pub_date = models.DateField()