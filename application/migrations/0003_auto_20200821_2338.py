# Generated by Django 2.2.15 on 2020-08-21 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20200821_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccination',
            name='rut',
            field=models.CharField(max_length=50),
        ),
    ]
