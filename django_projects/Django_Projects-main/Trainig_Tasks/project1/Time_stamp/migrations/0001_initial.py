# Generated by Django 2.2.28 on 2022-12-09 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stamp_models',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present_time', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
    ]
