# Generated by Django 3.2.23 on 2023-12-16 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0003_item_monday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.RemoveField(
            model_name='item',
            name='frequency',
        ),
        migrations.AddField(
            model_name='item',
            name='friday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='saturday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='sunday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='thursday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='tuesday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='wednesday',
            field=models.BooleanField(default=False),
        ),
    ]