from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):

    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name = "games")
    # gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
