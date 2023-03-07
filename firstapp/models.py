from django.db import models

# Create your models here.
class employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    sal = models.DecimalField(max_digits=10, decimal_places=3)
    def __str__(self):
        return self.name