# Generated by Django 2.2.28 on 2022-12-12 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_folder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='photo',
            new_name='images',
        ),
    ]
