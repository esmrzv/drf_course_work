from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitsValidator, HabitTimeValidator, related_validator, pleasant_filter_validator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitsValidator(field1='award', field2='related_habit'),
                      HabitTimeValidator(field1='time_to_complete'),
                      related_validator,
                      pleasant_filter_validator
                      ]

