# Generated by Django 2.2.13 on 2022-01-13 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220113_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]