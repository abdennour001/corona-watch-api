# Generated by Django 3.0.5 on 2020-04-05 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Declared',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_declaration', models.DateTimeField(auto_now_add=True)),
                ('id_treated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SuspectedCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_treated', models.BooleanField(default=False)),
            ],
        ),
    ]
