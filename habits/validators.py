from rest_framework import serializers


class HabitsValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        value_1 = value.get(self.field1)
        value_2 = value.get(self.field2)
        if value_1 and value_2:
            raise serializers.ValidationError(f'можно выбрать только одно поле')


class HabitTimeValidator:
    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, value):
        value_1 = value.get(self.field1)
        if value_1 >= 120:
            raise serializers.ValidationError(f'Время на выполнение не должно быть больше 120 секунд')


def related_validator(value):
    if value.get('related_habit'):
        if value.get('pleasant_habit') is not True:
            raise serializers.ValidationError(f'В связанные привычки могут попадать только привычки с признаком '
                                              f'приятной привычки.')


def pleasant_filter_validator(value):
    if value.get('pleasant_habit'):
        if value.get('award') and value.get('related_habit'):
            raise serializers.ValidationError(
                f'У приятной привычки не может быть вознаграждения или связанной привычки.')
