# Generated by Django 5.0.6 on 2024-05-27 16:56

import car_logistics.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_logistics', '0008_alter_lot_bos_alter_lot_photo_a_alter_lot_photo_d_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='photo_d',
            field=models.ImageField(blank=True, upload_to=car_logistics.models.unique_upload_path),
        ),
        migrations.AlterField(
            model_name='lot',
            name='photo_l',
            field=models.ImageField(blank=True, upload_to=car_logistics.models.unique_upload_path),
        ),
        migrations.AlterField(
            model_name='lot',
            name='photo_w',
            field=models.ImageField(blank=True, upload_to=car_logistics.models.unique_upload_path),
        ),
        migrations.AlterField(
            model_name='lot',
            name='title',
            field=models.FileField(blank=True, upload_to=car_logistics.models.unique_upload_path),
        ),
        migrations.AlterField(
            model_name='lot',
            name='video',
            field=models.FileField(blank=True, upload_to=car_logistics.models.unique_upload_path),
        ),
    ]
