# Generated by Django 5.0.6 on 2024-05-23 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_logistics', '0005_alter_lot_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='photo_d',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='lot',
            name='photo_w',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='lot',
            name='warehouse',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='car_logistics.warehouse'),
        ),
    ]