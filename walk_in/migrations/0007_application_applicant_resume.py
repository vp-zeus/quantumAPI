# Generated by Django 4.2.4 on 2023-08-30 05:38

from django.db import migrations, models
import walk_in.models


class Migration(migrations.Migration):

    dependencies = [
        ('walk_in', '0006_application_preferred_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='applicant_resume',
            field=models.FileField(blank=True, null=True, upload_to=walk_in.models.file_upload_to),
        ),
    ]
