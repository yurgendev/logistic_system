# Generated by Django 5.0.6 on 2024-06-09 08:27

import car_logistics.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_logistics', '0020_alter_document_lot_alter_image_lot_remove_lot_bos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='lot',
        ),
        migrations.RemoveField(
            model_name='video',
            name='lot',
        ),
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
        migrations.CreateModel(
            name='LotFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(choices=[('bos', 'BOS'), ('photo_a', 'Photo A'), ('photo_d', 'Photo D'), ('photo_w', 'Photo W'), ('video', 'Video'), ('title', 'Title'), ('photo_l', 'Photo L')], max_length=10)),
                ('file', models.FileField(blank=True, upload_to=car_logistics.models.unique_upload_path)),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='car_logistics.lot')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
