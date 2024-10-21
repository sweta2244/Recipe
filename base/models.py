from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='recipes/')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    process = models.TextField()
    ingredients = models.TextField()

    def __str__(self):
        return self.name
