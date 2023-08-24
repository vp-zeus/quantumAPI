# Generated by Django 4.2.4 on 2023-08-24 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.TextField()),
                ('address_line_1', models.TextField()),
                ('address_line_2', models.TextField()),
                ('city', models.CharField(max_length=45)),
                ('state', models.CharField(max_length=45)),
                ('pincode', models.CharField(max_length=45)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=45)),
                ('compensation', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.TextField()),
                ('address_line_1', models.TextField()),
                ('address_line_2', models.TextField()),
                ('city', models.CharField(max_length=45)),
                ('state', models.CharField(max_length=45)),
                ('pincode', models.CharField(max_length=45)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WalkIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('application_last_date', models.DateTimeField()),
                ('general_instructions', models.TextField()),
                ('instructions', models.TextField()),
                ('min_sys_requirements', models.TextField()),
                ('available_time_slots', models.ManyToManyField(related_name='walk_ins', to='walk_in.timeslot')),
                ('roles', models.ManyToManyField(related_name='walk_ins', to='walk_in.role')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='walk_ins', to='walk_in.venue')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
