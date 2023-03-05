# Generated by Django 4.1.5 on 2023-01-27 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_remove_newimage_about2'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateFoot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='UpdateFoot name')),
                ('about', models.TextField(verbose_name='UpdateFoot about')),
                ('about1', models.TextField(verbose_name='UpdateFoot about1')),
                ('about2', models.TextField(verbose_name='UpdateFoot about2')),
                ('about3', models.TextField(verbose_name='UpdateFoot about3')),
                ('about4', models.TextField(verbose_name='UpdateFoot about4')),
            ],
            options={
                'verbose_name': 'UpdateFoot',
                'verbose_name_plural': 'UpdateFoots',
            },
        ),
    ]
