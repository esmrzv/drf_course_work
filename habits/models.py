from django.db import models
from config import settings

PLEASANT_HABIT = (
    (True, "Да"),
    (False, "Нет"),
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
    reward = models.CharField(
        max_length=150,
        verbose_name="вознаграждение за выполнение привычки",
        null=True,
        blank=True,
    )
    pleasant_habit = models.BooleanField(
        choices=PLEASANT_HABIT, verbose_name="признак приятной привычки"
    )
    periodic_habit = models.PositiveIntegerField(
        default=1, verbose_name="преодичность выполнения"
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="связанная привычка",
        null=True,
        blank=True,
    )
    time_to_complete = models.PositiveSmallIntegerField(
        verbose_name="время на выполнение", default=120
    )
    is_public = models.BooleanField(default=False, verbose_name="публичность")
    last_reminder_date = models.DateTimeField(
        null=True, blank=True, verbose_name="Дата последнего напоминания"
    )

    def __str__(self):
        return f"{self.action} - {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
