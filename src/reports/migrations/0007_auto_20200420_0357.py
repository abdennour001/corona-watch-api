# Generated by Django 3.0.5 on 2020-04-20 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_auto_20200417_0819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='declared',
            name='id_treated',
        ),
        migrations.AddField(
            model_name='declared',
            name='is_treated',
            field=models.BooleanField(default=False),
        ),
    ]
