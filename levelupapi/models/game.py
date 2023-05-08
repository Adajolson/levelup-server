from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):

    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    number_of_players = models.IntegerField()
    skill_level = models.CharField(max_length=50)
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name = "games")
