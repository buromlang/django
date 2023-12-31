# Generated by Django 4.2.2 on 2023-07-04 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0006_alter_car_manufacturer'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerShip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relations.manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truck_name', models.CharField(max_length=100, null=True)),
                ('manufacturer', models.ManyToManyField(through='relations.PartnerShip', to='relations.manufacturer')),
            ],
        ),
        migrations.AddField(
            model_name='partnership',
            name='truck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relations.truck'),
        ),
    ]
