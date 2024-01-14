from django.db import models

# Create your models here.
class PostArgs(models.Model):
    text = models.CharField('text', max_length=20)

    class Meta:
        managed = False