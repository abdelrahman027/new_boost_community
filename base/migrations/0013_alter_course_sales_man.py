# Generated by Django 5.1.3 on 2024-11-11 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_course_trainer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Sales_man',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee', to='base.employee'),
        ),
    ]