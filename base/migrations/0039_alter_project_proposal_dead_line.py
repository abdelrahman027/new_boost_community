# Generated by Django 4.2.16 on 2024-12-20 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0038_comments_created_at_alter_comments_trainer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='proposal_dead_line',
            field=models.DateField(blank=True, default=datetime.date(2024, 12, 20), null=True),
        ),
    ]