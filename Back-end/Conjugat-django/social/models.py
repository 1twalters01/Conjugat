from django.db import models
from django.conf import settings
# from gqlalchemy import Memgraph, Node, Field, Edge

# db = settings.memgraph

# class User(Node):
#     user_ID: int = Field(unique=True, db=db)
#     last_online: date = Field(exist=True)

# class Following(models.Model):
#     following = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     following_created = models.DateTimeField(none=True, blank=True)
#     following_ended = models.DateTimeField(none=True, blank=True)
#     following_rank = models.IntegerField()

# class Followed(models.Model):
#     followed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     followed_by_created = models.ForeignKey()
#     followed_by_ended = models.DateTimeField()
#     followed_by_rank = models.IntegerField()

class Social(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    following = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    following_created = models.DateTimeField(none=True, blank=True)
    following_ended = models.DateTimeField(none=True, blank=True)
    follower_rank = models.IntegerField()
    Message_number = models.IntegerField()
    last_message = models.DateTimeField()
    battle_wins = models.IntegerField()
    battle_losses = models.IntegerField()
    battle_draws = models.IntegerField()
    last_battle = models.DateTimeField()
    class Meta:
        unique_together = (('user','following'),)
        indexes = [
        models.Index(fields=['follower_rank']),
        ]
    def __str__(self):
        return f'{self.user} is following by {self.following}'