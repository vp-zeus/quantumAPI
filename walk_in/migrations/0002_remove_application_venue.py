# Generated by Django 4.2.4 on 2023-08-27 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('walk_in', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='venue',
        ),
    ]
