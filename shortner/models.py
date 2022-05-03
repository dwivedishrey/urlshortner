from django.db import models
class url(models.Model):
    link=models.CharField(max_length=10000)
    uvid=models.CharField(max_length=10)
# Create your models here.
