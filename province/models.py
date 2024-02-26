from django.db import models

# Create your models here.
from django.db import models

class Province(models.Model):
    id = models.AutoField(primary_key=True)
    province = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.province
