# Generated by Django 4.2.16 on 2024-12-21 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0006_rename_date_flight_departure_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='departure_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]