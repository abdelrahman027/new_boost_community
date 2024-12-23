# Generated by Django 4.2.16 on 2024-12-20 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Halls',
            fields=[
                ('hall_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('hotel_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('rating', models.FloatField()),
                ('hall', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='venues.halls')),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=255)),
                ('Hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='venues.hotels')),
            ],
        ),
    ]
