# Generated by Django 5.0.6 on 2024-05-23 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_logistics', '0002_alter_company_options_lot_status_changed_account_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='lot',
            name='auction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_logistics.auction'),
        ),
    ]
