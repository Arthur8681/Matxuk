from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Habits(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.TextField()
    repeat_time = models.IntegerField
    times_per_day = models.IntegerField
    max_streaks_days = models.IntegerField
    is_active = models.BooleanField


class habit_completions(models.model):
    habit_id = models.ForeignKey(Habits, on_delete=models.CASCADE)
    completed_at = models.DateTimeField


class tags(models.model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

class habit_tags(models.model):
    habit_id = models.ForeignKey(Habits, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(tags, on_delete=models.CASCADE)



