# Generated by Django 5.0.6 on 2024-05-23 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_logistics', '0004_lot_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='url',
            field=models.URLField(),
        ),
    ]
