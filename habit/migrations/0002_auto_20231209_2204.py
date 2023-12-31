# Generated by Django 3.2.23 on 2023-12-09 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='item',
            name='frequency',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='HabitUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
                ('shared_users', models.ManyToManyField(blank=True, to='habit.Item')),
            ],
        ),
    ]
