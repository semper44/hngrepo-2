from django.db import models

# Create your models here.
class hngapi(models.Model):
    username=models.CharField(max_length=50)
    backend=models.BooleanField()
    age=models.IntegerField()
    bio=models.TextField()
