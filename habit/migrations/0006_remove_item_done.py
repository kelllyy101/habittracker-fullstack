# Generated by Django 3.2.23 on 2023-12-19 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0005_item_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='done',
        ),
    ]
