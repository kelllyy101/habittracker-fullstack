from django.db import models

# Create your models here.


class Item(models.Model):
    user_id = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
    monday = models.BooleanField(null=False, blank=False, default=False)
    tuesday = models.BooleanField(null=False, blank=False, default=False)
    wednesday = models.BooleanField(null=False, blank=False, default=False)
    thursday = models.BooleanField(null=False, blank=False, default=False)
    friday = models.BooleanField(null=False, blank=False, default=False)
    saturday = models.BooleanField(null=False, blank=False, default=False)
    sunday = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name


class HabitUsers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField('User Email')
    shared_users = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

