from rest_framework import serializers


class HabitsValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        value_1 = value.get(self.field1)
        value_2 = value.get(self.field2)
        if value_1 and value_2:
            raise serializers.ValidationError("можно выбрать только одно поле")


class HabitTimeValidator:
    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, value):
        value_1 = value.get(self.field1)
        if value_1 >= 120:
            raise serializers.ValidationError(
                "Время на выполнение не должно быть больше 120 секунд"
            )


def related_validator(value):
    if value.get("related_habit"):
        if not value.get("pleasant_habit"):
            raise serializers.ValidationError(
                "В связанные привычки могут попадать только привычки с признаком "
                "приятной привычки."
            )


def pleasant_filter_validator(value):
    if value.get("pleasant_habit"):
        if value.get("reward") or value.get("related_habit"):
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки"
                "нельзя одновременно указать связанную привычку и вознаграждение."
            )


class HabitFilterTimeValidator:
    def __init__(self, min_date=1, max_date=7):
        self.min_date = min_date
        self.max_date = max_date

    def __call__(self, value):
        periodic_habit = dict(value).get("periodic_habit")
        if int(periodic_habit) <= self.min_date or int(periodic_habit) > self.max_date:
            raise serializers.ValidationError(
                "Нельзя выполнять привычку реже, чем 1 раз в 7 дней"
            )
