# Generated by Django 4.0.4 on 2022-08-26 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detectTrash', '0002_alter_locations_pub_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locations',
            old_name='pub_date',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='locations',
            old_name='question_text',
            new_name='longititude',
        ),
    ]