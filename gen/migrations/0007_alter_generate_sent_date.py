# Generated by Django 3.2 on 2022-08-07 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen', '0006_alter_generate_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generate',
            name='sent_date',
            field=models.TimeField(auto_now_add=True, default=''),
            preserve_default=False,
        ),
    ]
