# Generated by Django 3.2 on 2022-08-06 18:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='generate',
            name='sent_date',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
