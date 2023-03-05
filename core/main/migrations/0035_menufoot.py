# Generated by Django 4.1.5 on 2023-01-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_dinnerimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuFoot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='MenuFoot name')),
                ('name1', models.CharField(max_length=50, verbose_name='MenuFoot name1')),
                ('name2', models.CharField(max_length=50, verbose_name='MenuFoot name2')),
                ('name3', models.CharField(max_length=50, verbose_name='MenuFoot name3')),
                ('name4', models.CharField(max_length=50, verbose_name='MenuFoot name4')),
                ('about', models.TextField(verbose_name='MenuFoot about')),
                ('about1', models.TextField(verbose_name='MenuFoot about1')),
                ('about2', models.TextField(verbose_name='MenuFoot about2')),
                ('about3', models.TextField(verbose_name='MenuFoot about3')),
                ('about4', models.TextField(verbose_name='MenuFoot about4')),
            ],
            options={
                'verbose_name': 'MenuFoot',
                'verbose_name_plural': 'MenuFoots',
            },
        ),
    ]