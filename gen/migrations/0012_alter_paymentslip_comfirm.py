# Generated by Django 3.2 on 2022-08-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen', '0011_paymentslip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentslip',
            name='comfirm',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
