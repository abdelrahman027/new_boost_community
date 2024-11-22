# Generated by Django 4.2.16 on 2024-11-13 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_course_facilitator_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='certificate',
        ),
        migrations.AddField(
            model_name='certificate',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.course'),
        ),
    ]