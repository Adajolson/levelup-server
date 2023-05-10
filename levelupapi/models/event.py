from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):

    description = models.CharField(max_length=155)
    date = models.DateField()
    time = models.TimeField()
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="organized_events")
    game = models.ForeignKey("Game", on_delete=models.CASCADE,)
    attendees = models.ManyToManyField("Gamer")

