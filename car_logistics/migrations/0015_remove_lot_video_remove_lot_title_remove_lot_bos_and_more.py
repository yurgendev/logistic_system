# Generated by Django 5.0.6 on 2024-06-07 07:47

import car_logistics.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_logistics', '0014_alter_lot_bos_alter_lot_photo_a_alter_lot_photo_d_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lot',
            name='video',
        ),
        migrations.RemoveField(
            model_name='lot',
            name='title',
        ),
        migrations.RemoveField(
            model_name='lot',
            name='bos',
        ),
        migrations.RemoveField(
            model_name='lot',
            name='photo_w',
        ),
        migrations.RemoveField(
            model_name='lot',
            name='photo_l',
        ),
        migrations.RemoveField(
            model_name='lot',
            name='photo_a',
        ),
        migrations.RemoveField(
            model_name='lot',
            name='photo_d',
        ),
        migrations.AddField(
            model_name='lot',
            name='video',
            field=models.FileField(blank=True, upload_to=car_logistics.models.unique_upload_path),
        ),
        migrations.AddField(
            model_name='lot',
            name='title',
            field=models.FileField(blank=True, upload_to=car_logistics.models.unique_upload_path),
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.AddField(
            model_name='lot',
            name='bos',
            field=models.FileField(blank=True, null=True, upload_to=car_logistics.models.unique_upload_path),
        ),
        migrations.AddField(
            model_name='lot',
            name='photo_w',
            field=models.ImageField(blank=True, upload_to=car_logistics.models.unique_upload_path),
        ),
        migrations.AddField(
            model_name='lot',
            name='photo_l',
            field=models.ImageField(blank=True, upload_to=car_logistics.models.unique_upload_path),
        ),
        migrations.AddField(
            model_name='lot',
            name='photo_a',
            field=models.ImageField(blank=True, null=True, upload_to=car_logistics.models.unique_upload_path),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='lot',
            name='photo_d',
            field=models.ImageField(blank=True, upload_to=car_logistics.models.unique_upload_path),
        ),
    ]
