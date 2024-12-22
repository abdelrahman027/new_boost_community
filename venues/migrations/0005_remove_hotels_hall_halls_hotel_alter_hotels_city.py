# Generated by Django 4.2.16 on 2024-12-20 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0004_hotels_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='hall',
        ),
        migrations.AddField(
            model_name='halls',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='venues.hotels'),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='venues.city'),
        ),
    ]
