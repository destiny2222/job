# Generated by Django 3.2 on 2022-08-07 14:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gen', '0007_alter_generate_sent_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generate',
            name='sent_date',
            field=models.TimeField(auto_now_add=django.utils.timezone.now),
        ),
    ]