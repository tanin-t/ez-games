from django.db import models


class BingoNumber(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)


class Player(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'Player: {self.name} ({self.pk})'
