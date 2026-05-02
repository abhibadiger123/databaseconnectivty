from django.db import models

# Create your models here.

class Drinks(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    quantity = models.IntegerField(default=2)

    def __str__(self):
        return self.name