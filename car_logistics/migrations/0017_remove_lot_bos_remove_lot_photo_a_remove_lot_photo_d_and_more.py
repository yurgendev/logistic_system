# Generated by Django 5.0.6 on 2024-06-07 09:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_logistics', '0016_document_image_remove_lot_bos_remove_lot_photo_a_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lot',
            name='bos',
        ),
        migrations.RemoveField(
            model_name='lot',
            name='photo_a',
        ),
        migrations.RemoveField(
            model_name='lot',
            name='photo_d',
        ),
        migrations.RemoveField(
            model_name='lot',
            name='photo_l',
        ),
        migrations.RemoveField(
            model_name='lot',
            name='photo_w',
        ),
        migrations.RemoveField(
            model_name='lot',
            name='title',
        ),
        migrations.RemoveField(
            model_name='lot',
            name='video',
        ),
        migrations.AddField(
            model_name='document',
            name='lot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='car_logistics.lot'),
        ),
        migrations.AddField(
            model_name='image',
            name='lot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='car_logistics.lot'),
        ),
    ]
