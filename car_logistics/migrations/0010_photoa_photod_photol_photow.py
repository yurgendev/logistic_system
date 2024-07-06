# Generated by Django 5.0.6 on 2024-06-01 09:00

import car_logistics.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_logistics', '0009_alter_lot_photo_d_alter_lot_photo_l_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=car_logistics.models.unique_upload_path)),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_a_images', to='car_logistics.lot')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=car_logistics.models.unique_upload_path)),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_d_images', to='car_logistics.lot')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=car_logistics.models.unique_upload_path)),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_l_images', to='car_logistics.lot')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=car_logistics.models.unique_upload_path)),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_w_images', to='car_logistics.lot')),
            ],
        ),
    ]