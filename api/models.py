from django.db import models

# Create your models here.
class PostArgs(models.Model):
    text = models.CharField(max_length=20)