# Generated by Django 5.1.3 on 2024-11-11 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_course_number_of_gift'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
