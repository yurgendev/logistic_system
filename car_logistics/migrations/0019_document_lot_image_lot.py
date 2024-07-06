# Generated by Django 5.0.6 on 2024-06-08 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_logistics', '0018_remove_document_lot_remove_image_lot_lot_bos_and_more'),
    ]

    operations = [
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