# Generated by Django 4.0.4 on 2022-08-27 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detectTrash', '0006_locations_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locations',
            name='date',
        ),
    ]