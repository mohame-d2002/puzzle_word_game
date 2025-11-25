from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # link to current user
    level_progress = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - Level {self.level_progress}"
