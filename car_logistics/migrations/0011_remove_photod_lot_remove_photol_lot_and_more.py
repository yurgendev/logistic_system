# Generated by Django 5.0.6 on 2024-06-01 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_logistics', '0010_photoa_photod_photol_photow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photod',
            name='lot',
        ),
        migrations.RemoveField(
            model_name='photol',
            name='lot',
        ),
        migrations.RemoveField(
            model_name='photow',
            name='lot',
        ),
        migrations.DeleteModel(
            name='PhotoA',
        ),
        migrations.DeleteModel(
            name='PhotoD',
        ),
        migrations.DeleteModel(
            name='PhotoL',
        ),
        migrations.DeleteModel(
            name='PhotoW',
        ),
    ]