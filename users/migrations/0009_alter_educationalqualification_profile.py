# Generated by Django 4.2.4 on 2023-08-28 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_educationalqualification_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationalqualification',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='educational_qualification', to='users.profile'),
        ),
    ]
