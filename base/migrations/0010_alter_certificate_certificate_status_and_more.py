# Generated by Django 5.1.3 on 2024-11-11 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_rename_deparment_name_department_department_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='certificate_status',
            field=models.CharField(choices=[('online', 'Online'), ('physical', 'Physical')], max_length=40),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_category',
            field=models.CharField(choices=[('online', 'Online'), ('physical', 'Physical')], max_length=40, null=True),
        ),
    ]