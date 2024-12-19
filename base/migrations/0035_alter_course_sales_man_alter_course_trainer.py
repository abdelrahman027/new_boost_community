# Generated by Django 4.2.16 on 2024-12-18 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0002_visa_trainers_hotel_flight'),
        ('base', '0034_alter_project_proposal_dead_line_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Sales_man',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales', to='base.employee'),
        ),
        migrations.AlterField(
            model_name='course',
            name='trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses', to='trainers.trainer'),
        ),
    ]
