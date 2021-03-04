# Generated by Django 3.1.6 on 2021-03-04 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0006_auto_20210303_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(1, 'General'), (2, 'Holidays'), (3, 'Food'), (4, 'Car'), (5, 'Living'), (6, 'Hobbies'), (7, 'Shopping'), (8, 'Education'), (9, 'Health')], default=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Low'), (2, 'Normal'), (3, 'High')], default=1),
        ),
    ]
