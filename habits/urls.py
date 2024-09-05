from django.urls import path

from habits import views
from habits.apps import HabitsConfig

app_name = HabitsConfig.name
urlpatterns = [
    path('list/', views.HabitListAPIView.as_view(), name='list'),
    path('<int:pk>/update/', views.HabitUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.HabitDeleteAPIView.as_view(), name='delete'),
    path('<int:pk>/detail/', views.HabitDetailAPIView.as_view(), name='detail'),
    path('create/', views.HabitCreateAPIView.as_view(), name='create'),
    path('public-list/', views.HabitPublicListAPIView.as_view(), name='public-list'),
]
