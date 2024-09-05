from datetime import timedelta

from django.db import models
from config import settings

PLEASANT_HABIT = (
    (True, "Да"),
    (False, "Нет"),
)
PERIODIC_HABIT = (
    ("daily", "Ежедневно"),
    ("in a day", "Через день"),
    ("in a two days", "Раз в три дня"),
    ("weekly", "Раз в неделю"),
)


class Habit(models.Model):
    place = models.CharField(max_length=100, verbose_name="место")
    time = models.TimeField(verbose_name="время, когда нужно выполнить привычку")
    action = models.CharField(max_length=150, verbose_name="действие")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="пользователь привычки",
    )
    award = models.CharField(
        max_length=150, verbose_name="вознаграждение за выполнение привычки", null=True, blank=True
    )
    pleasant_habit = models.BooleanField(
        choices=PLEASANT_HABIT, verbose_name="признак приятной привычки"
    )
    periodic_habit = models.CharField(
        max_length=100, choices=PERIODIC_HABIT, verbose_name="преодичность выполнения"
    )
    related_habit = models.ForeignKey(
        "self", on_delete=models.CASCADE, verbose_name="связанная привычка", null=True, blank=True
    )
    time_to_complete = models.PositiveSmallIntegerField(
        verbose_name="время на выполнение", default=120
    )
    is_public = models.BooleanField(default=False, verbose_name="публичность")

    def __str__(self):
        return f'{self.action} - {self.place}'

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
