# Generated by Django 4.2.16 on 2024-12-21 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0002_visa_trainers_hotel_flight'),
    ]

    operations = [
        migrations.AddField(
            model_name='visa',
            name='vis_pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdf'),
        ),
    ]
