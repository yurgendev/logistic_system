# Generated by Django 5.0.6 on 2024-05-22 08:20

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_logistics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies WH'},
        ),
        migrations.AddField(
            model_name='lot',
            name='status_changed',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 5, 22, 8, 20, 2, 805169)),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='car_logistics.customer')),
            ],
        ),
        migrations.AlterField(
            model_name='lot',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_logistics.account'),
        ),
    ]
