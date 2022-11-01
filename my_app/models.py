from django.db import models

class Meca(models.Model):
    name = models.CharField(max_length=30)
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.ano}"
        
class Segundo(models.Model):
    name = models.CharField(max_length=30)
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.ano}"

# Create your models here.
