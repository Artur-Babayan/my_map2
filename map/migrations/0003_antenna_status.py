# Generated by Django 4.2 on 2023-04-14 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_alter_antenna_latitude_alter_antenna_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='antenna',
            name='status',
            field=models.CharField(default='up', max_length=10),
        ),
    ]