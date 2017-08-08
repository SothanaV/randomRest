from django.db import models

# Create your models here.
class Rest(models.Model):
    no    = models.IntegerField(default=0)
    rest    = models.CharField(default=0,max_length=20)
    class Meta:
        ordering = ['no']