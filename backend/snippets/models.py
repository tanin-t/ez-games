from django.db import models


class Snippet(models.Model):
    question = models.CharField(max_length=500)
    choice1 = models.CharField(max_length=500)
    choice2 = models.CharField(max_length=500)
    choice3 = models.CharField(max_length=500)
    choice4 = models.CharField(max_length=500)

    CHOICES = (
        ("1", "Choice 1"),
        ("2", "Choice 2"),
        ("3", "Choice 3"),
        ("4", "Choice 4"),
    )

    answer = models.CharField(
        max_length=1,
        choices=CHOICES,
        default="1",
    )

    def __str__(self) -> str:
        return self.question


class Highest(models.Model):
    name = models.CharField(max_length=255)
    score = models.IntegerField(default=1)
    input = models.BooleanField(default=False)
