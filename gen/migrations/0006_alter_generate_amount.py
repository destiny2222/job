# Generated by Django 3.2 on 2022-08-07 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen', '0005_auto_20220807_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generate',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=225),
        ),
    ]