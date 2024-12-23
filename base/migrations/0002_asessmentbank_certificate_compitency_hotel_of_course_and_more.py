# Generated by Django 5.1.3 on 2024-11-10 19:06

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsessmentBank',
            fields=[
                ('asessement_id', models.AutoField(primary_key=True, serialize=False)),
                ('asessment_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('assessment_file', models.FileField(blank=True, null=True, upload_to='pdf')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('course_name', models.CharField(max_length=255)),
                ('certificate_id', models.AutoField(primary_key=True, serialize=False)),
                ('certificate_status', models.CharField(choices=[('online', 'Public Course'), ('physical', 'Private Course')], max_length=40)),
                ('certificates_file', models.FileField(blank=True, null=True, upload_to='pdf')),
            ],
        ),
        migrations.CreateModel(
            name='Compitency',
            fields=[
                ('compitency_id', models.AutoField(primary_key=True, serialize=False)),
                ('compitency_name', models.CharField(max_length=255)),
                ('compitency_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_of_course',
            fields=[
                ('hotel_id', models.AutoField(primary_key=True, serialize=False)),
                ('hotel_name', models.CharField(max_length=255)),
                ('hotel_location', models.CharField(max_length=255)),
                ('course_name', models.CharField(max_length=255)),
                ('review', models.CharField(default='0', max_length=255)),
                ('contact_person', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inventory_id', models.AutoField(primary_key=True, serialize=False)),
                ('descripttion', models.TextField(blank=True, null=True)),
                ('quantity', models.CharField(max_length=100)),
                ('branch', models.CharField(choices=[('Dubai', 'Dubai'), ('Abu Dhabi', 'Abu Dhabi'), ('Egypt', 'Egypt'), ('KSA', 'Ksa')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Logestics',
            fields=[
                ('logestic_id', models.AutoField(primary_key=True, serialize=False)),
                ('driver_name', models.CharField(max_length=255)),
                ('driver_phone', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('material_id', models.AutoField(primary_key=True, serialize=False)),
                ('material_name', models.CharField(max_length=255)),
                ('maerial_status', models.CharField(choices=[('Receieved', 'Received Material'), ('Ready for Design', 'Ready For Design'), ('Ready to Print', 'Ready For Print'), ('printed and Ready for Delivery', 'Ready For Delivery'), ('Delivred', 'Delivered')], max_length=40)),
                ('material_file', models.FileField(blank=True, null=True, upload_to='pdf')),
                ('material_notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='manager',
        ),
        migrations.AddField(
            model_name='course',
            name='Sales_man',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.employee'),
        ),
        migrations.AddField(
            model_name='course',
            name='contract',
            field=models.FileField(blank=True, null=True, upload_to='pdf'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_Date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_category',
            field=models.CharField(choices=[('online', 'Public Course'), ('physical', 'Private Course')], max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_confirmation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='course_duration',
            field=models.CharField(default='1', max_length=2),
        ),
        migrations.AddField(
            model_name='course',
            name='course_name',
            field=models.CharField(default='New Course', max_length=255),
        ),
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.CharField(choices=[('Public', 'Public Course'), ('Private', 'Private Course')], max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='field',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='gift_items_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='invoice',
            field=models.FileField(blank=True, null=True, upload_to='pdf'),
        ),
        migrations.AddField(
            model_name='course',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='number_of_attendees',
            field=models.CharField(default='1', max_length=2),
        ),
        migrations.AddField(
            model_name='course',
            name='pre_post_files',
            field=models.FileField(blank=True, null=True, upload_to='pdf'),
        ),
        migrations.AddField(
            model_name='course',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.project'),
        ),
        migrations.AddField(
            model_name='course',
            name='trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.trainer'),
        ),
        migrations.AddField(
            model_name='course',
            name='trainer_visa_valid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='manager_role',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='points',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='trainer',
            name='account_branch',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='account_currency',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='bank_account_number',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='bank_swift_code',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='passport_scan',
            field=models.FileField(blank=True, null=True, upload_to='pdf'),
        ),
        migrations.AlterField(
            model_name='project',
            name='starting_Date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('badge_id', models.AutoField(primary_key=True, serialize=False)),
                ('issue_date', models.DateField()),
                ('badge_name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('badge_img', models.ImageField(blank=True, default='employee_photos/default-employee.webp', null=True, upload_to='employee_photos/')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.employee')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='certificate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.certificate'),
        ),
        migrations.CreateModel(
            name='Design_Request',
            fields=[
                ('design_request_id', models.AutoField(primary_key=True, serialize=False)),
                ('design_type', models.CharField(choices=[('Materials', 'Materials'), ('Persentation', 'Persentation'), ('Proposal', 'Proposal'), ('Ui', 'Ui'), ('banner', 'Banner'), ('other', 'Other')], max_length=255)),
                ('design_file', models.FileField(blank=True, null=True, upload_to='pdf')),
                ('comments', models.TextField(blank=True, null=True)),
                ('requested_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Facilitator',
            fields=[
                ('facilitator_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.employee')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='facilitator',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.facilitator'),
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_to', models.DateField(auto_now_add=True)),
                ('Ticket', models.FileField(blank=True, null=True, upload_to='pdf')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.course')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.trainer')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.hotel_of_course'),
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('idea_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('points', models.CharField(blank=True, max_length=20, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manger_id', models.AutoField(primary_key=True, serialize=False)),
                ('deparment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.department')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.employee')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='materials',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.material'),
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('portfolio_id', models.AutoField(primary_key=True, serialize=False)),
                ('template_name', models.CharField(max_length=255)),
                ('description_of_template', models.TextField(blank=True, null=True)),
                ('Template_file', models.FileField(blank=True, null=True, upload_to='pdf')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.project')),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('repository_id', models.AutoField(primary_key=True, serialize=False)),
                ('document_name', models.CharField(max_length=255)),
                ('repo_file', models.FileField(blank=True, null=True, upload_to='pdf')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.project')),
            ],
        ),
        migrations.CreateModel(
            name='Simulation',
            fields=[
                ('simulation_id', models.AutoField(primary_key=True, serialize=False)),
                ('Simulation_name', models.CharField(max_length=255)),
                ('simulation_photo', models.ImageField(blank=True, default='employee_photos/default-employee.webp', null=True, upload_to='employee_photos/')),
                ('learning_guide', models.FileField(blank=True, null=True, upload_to='pdf')),
                ('compitency', models.ManyToManyField(to='base.compitency')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Done', 'Done'), ('Stuck', 'Stuck'), ('In Progress', 'In Progress'), ('Missed', 'Missed')], max_length=50)),
                ('deadline', models.DateField()),
                ('points', models.CharField(max_length=20)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.department')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.employee')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.manager')),
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
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.course')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='Visa',
            fields=[
                ('visa_id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Applied', 'Applied'), ('Processing', 'Processing'), ('Issued', 'Issued')], max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.course')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.trainer')),
            ],
        ),
    ]
