from celery import shared_task
from datetime import timedelta

from django.utils import timezone
from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_tg_message():
    time_now = timezone.localtime()
    # Получаем привычки, которые нужно напомнить
    habits = Habit.objects.filter(
        time__gt=time_now, time__lt=time_now + timedelta(minutes=1)
    )

    for habit in habits:
        # Проверяем, нужно ли отправлять напоминание на основе периодичности
        last_reminder_date = habit.last_reminder_date or timezone.now() - timedelta(
            days=habit.periodic_habit
        )
        if (timezone.now() - last_reminder_date).days >= habit.periodic_habit:
            send_telegram_message(
                habit.user.tg_chat_id,
                f"Напоминание о выполнении привычки в {habit.time}",
            )
            habit.last_reminder_date = (
                timezone.now()
            )  # Обновляем дату последнего напоминания
            habit.save()
