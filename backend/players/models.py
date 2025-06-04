from django.contrib.auth.models import User
from django.db import models

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='player_profile')
    date_of_birth = models.DateField(null=True, blank=True)
    playing_hand = models.CharField(max_length=10, choices=[('left', 'Left'), ('right', 'Right')], default='right')
    rating = models.FloatField(default=1000.0)  # Elo rating starting value

    def __str__(self):
        return self.user.username
