# Generated by Django 3.0.5 on 2020-04-05 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('attachments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('publication_date', models.DateTimeField()),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.Publication')),
            ],
            options={
                'ordering': ['comment_date'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('publication_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feeds.Publication')),
                ('description', models.TextField()),
                ('attachment', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='attachments.Attachment')),
            ],
            bases=('feeds.publication',),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('publication_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feeds.Publication')),
                ('content', models.TextField()),
                ('attachment', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='attachments.Attachment')),
            ],
            bases=('feeds.publication',),
        ),
    ]
