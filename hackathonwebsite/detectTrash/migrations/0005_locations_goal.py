# Generated by Django 4.0.4 on 2022-08-27 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detectTrash', '0004_rename_longititude_locations_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='goal',
            field=models.IntegerField(default=10),
        ),
    ]
