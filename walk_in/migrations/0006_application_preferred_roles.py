# Generated by Django 4.2.4 on 2023-08-29 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('walk_in', '0005_remove_application_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='preferred_roles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='walk_in.role'),
        ),
    ]
