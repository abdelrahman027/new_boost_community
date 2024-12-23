# Generated by Django 4.2.16 on 2024-11-22 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visa',
            fields=[
                ('visa_id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Applied', 'Applied'), ('Processing', 'Processing'), ('Issued', 'Issued')], max_length=100)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainers.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='Trainers_hotel',
            fields=[
                ('hotel_id', models.AutoField(primary_key=True, serialize=False)),
                ('hotel_name', models.CharField(max_length=255)),
                ('hotel_location', models.CharField(max_length=255)),
                ('number_of_night', models.CharField(max_length=2)),
                ('reservation_date', models.DateField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid')], max_length=255)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainers.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_to', models.DateField(auto_now_add=True)),
                ('Ticket', models.FileField(blank=True, null=True, upload_to='pdf')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainers.trainer')),
            ],
        ),
    ]
