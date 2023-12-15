from django.apps import AppConfig


class HabitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'habit'


def habits_display(habits):
    return [
        {
            "id": habit.id,
            "name": habit.description,
            "frequency": " - ".join([days[int(day)] for day in habit.frequency.split()])
        } for habit in habits
    ]
