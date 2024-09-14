from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@test.com", first_name="test", last_name="testov"
        )
        self.habit = Habit.objects.create(
            place="room",
            time="14:00:00",
            action="подтягвания",
            reward="деньги",
            pleasant_habit=True,
            periodic_habit=1,
            time_to_complete=100,
            is_public=True,
            user=self.user,
            related_habit=None,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_detail(self):
        url = reverse("habits:detail", args=[self.habit.pk])
        response = self.client.get(url)
        data = response.json()
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), self.habit.place)
        self.assertEqual(data.get("action"), self.habit.action)
        self.assertEqual(data.get("reward"), self.habit.reward)
        self.assertEqual(data.get("user"), self.habit.user.pk)
        self.assertEqual(data.get("time_to_complete"), self.habit.time_to_complete)
        self.assertEqual(data.get("is_public"), self.habit.is_public)
        self.assertEqual(data.get("related_habit"), self.habit.related_habit)

    def test_habit_update(self):
        url = reverse("habits:update", args=[self.habit.pk])
        data = {
            "place": "bathroom",
            "time": "13:00:00",
            "action": "скука",
            "time_to_complete": 20,
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), "bathroom")
        self.assertEqual(data.get("time"), "13:00:00")
        self.assertEqual(data.get("action"), "скука")
        self.assertEqual(data.get("time_to_complete"), 20)

    def test_habit_delete(self):
        url = reverse("habits:delete", args=[self.habit.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_create(self):
        url = reverse("habits:create")
        content = {
            "place": "bathroom",
            "time": "14:00:00",
            "action": "подтягвания",
            "user": self.habit.user.pk,
            "time_to_complete": 100,
            "is_public": True,
            "pleasant_habit": False,
            "periodic_habit": 2,
        }

        response = self.client.post(url, content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_list_all(self):
        url = reverse("habits:list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "place": "room",
                    "time": "14:00:00",
                    "action": "подтягвания",
                    "reward": "деньги",
                    "pleasant_habit": True,
                    "periodic_habit": 1,
                    "time_to_complete": 100,
                    "is_public": True,
                    "last_reminder_date": None,
                    "user": self.user.pk,
                    "related_habit": None,
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 1)
        self.assertEqual(data, result)
