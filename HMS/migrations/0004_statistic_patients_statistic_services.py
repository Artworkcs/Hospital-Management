# Generated by Django 4.1.6 on 2023-07-24 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0003_statistic_doctors_statistic_nurses'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='Patients',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='statistic',
            name='Services',
            field=models.IntegerField(null=True),
        ),
    ]