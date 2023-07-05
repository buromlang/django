# Generated by Django 4.2.2 on 2023-07-04 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0007_partnership_truck_partnership_truck'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnership',
            name='manufacturer1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='relations.manufacturer'),
        ),
        migrations.AlterField(
            model_name='partnership',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manufacturer', to='relations.manufacturer'),
        ),
    ]
