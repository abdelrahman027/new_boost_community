# Generated by Django 4.2.16 on 2024-12-19 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0002_visa_trainers_hotel_flight'),
        ('base', '0037_alter_project_proposal_dead_line_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='trainers.trainer'),
        ),
    ]
