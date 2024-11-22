# Generated by Django 4.2.16 on 2024-11-12 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_project_invoice_remove_proposal_client_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_invoice',
        ),
        migrations.RemoveField(
            model_name='project',
            name='proposal',
        ),
        migrations.RemoveField(
            model_name='project',
            name='request_for_proposal',
        ),
        migrations.AddField(
            model_name='project',
            name='invoice_document',
            field=models.FileField(blank=True, null=True, upload_to='pdf'),
        ),
        migrations.AddField(
            model_name='project',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='invoice_status',
            field=models.CharField(choices=[('accepted', 'Accepted'), ('issued', 'Issued'), ('paid', 'Paid'), ('waiting papers', 'Waiting Papers')], default='accepted', max_length=20),
        ),
        migrations.AddField(
            model_name='project',
            name='proposal_dead_line',
            field=models.DateField(blank=True, default=datetime.date(2024, 11, 12), null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='proposal_document',
            field=models.FileField(blank=True, null=True, upload_to='pdf'),
        ),
        migrations.AddField(
            model_name='project',
            name='proposal_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='proposal_status',
            field=models.CharField(choices=[('recieved', 'Recieved'), ('pricing', 'Pricing'), ('priced', 'Priced'), ('sent', 'Sent')], default='recieved', max_length=20),
        ),
        migrations.AddField(
            model_name='project',
            name='rfp_document',
            field=models.FileField(blank=True, null=True, upload_to='pdf'),
        ),
        migrations.AddField(
            model_name='project',
            name='rfp_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Project_invoice',
        ),
        migrations.DeleteModel(
            name='Proposal',
        ),
        migrations.DeleteModel(
            name='Request_for_proposal',
        ),
    ]
