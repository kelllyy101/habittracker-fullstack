from django.apps import AppConfig


class HabitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'habit'

days = {
    0: "Sun",
    1: "Mon",
    2: "Tues",
    3: "Wed",
    4: "Thurs",
    5: "Fri",
    6: "Sat",
}


def habits_display(items):
    return [
        {
            "id": item.id,
            "name": item.description,
            "frequency": " - ".join([days[int(day)] for day in item.frequency.split()])
        } for item in items
    ]

