# Generated by Django 4.2.4 on 2023-08-29 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_profile_resume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professionalqualification',
            old_name='type',
            new_name='applicant_type',
        ),
    ]
