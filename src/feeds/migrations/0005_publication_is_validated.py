# Generated by Django 3.0.5 on 2020-04-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_video_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='is_validated',
            field=models.BooleanField(default=False),
        ),
    ]