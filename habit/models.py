from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
    description = models.TextField(max_length=200, blank=True)
    frequency = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name


class HabitUsers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField('User Email')
    shared_users = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

