# Generated by Django 4.0.4 on 2022-08-27 08:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('detectTrash', '0005_locations_goal'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
