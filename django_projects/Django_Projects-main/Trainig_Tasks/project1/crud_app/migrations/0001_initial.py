# Generated by Django 2.2.28 on 2022-12-09 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
