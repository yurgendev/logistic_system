# Generated by Django 5.0.6 on 2024-05-23 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_logistics', '0006_alter_lot_photo_d_alter_lot_photo_w_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='car_logistics.warehouse'),
        ),
    ]
