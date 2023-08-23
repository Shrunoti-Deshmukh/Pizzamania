from django.db import models

class recipe(models.Model):
    image = models.CharField(max_length=100)
    cat = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    ing = models.TextField()
    des = models.TextField()
# Create your models here.
