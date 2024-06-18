from django.db import models # type: ignore

# Create your models here.


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type1 = models.CharField(max_length=50)
    type2 = models.CharField(max_length=50, blank=True, null=True)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()
    
    def __str__(self):
        return self.name