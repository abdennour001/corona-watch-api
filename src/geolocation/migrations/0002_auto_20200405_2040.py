# Generated by Django 3.0.5 on 2020-04-05 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geolocation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='reception_center',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='geolocation.ReceptionCenter'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receptioncenter',
            name='region',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='geolocation.Region'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='region',
            name='location',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='geolocation.Location'),
            preserve_default=False,
        ),
    ]
