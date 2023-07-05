# Generated by Django 4.2.2 on 2023-06-30 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='vehicle_choice',
            field=models.CharField(choices=[('C', 'Car'), ('T', 'Truck'), ('J', 'Jet Ski')], default='C', max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='year_in_school',
            field=models.CharField(choices=[('Audio', (('vinyl', 'Vinyl'), ('cd', 'CD'))), ('Video', (('vhs', 'VHS Tape'), ('dvd', 'DVD'))), ('unknown', 'Unknown')], max_length=8),
        ),
    ]