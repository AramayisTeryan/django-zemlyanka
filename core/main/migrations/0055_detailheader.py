# Generated by Django 4.1.5 on 2023-01-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0054_contactrevers'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='DetailHeader name')),
                ('about', models.TextField(verbose_name='DetailHeader about')),
                ('about1', models.TextField(verbose_name='DetailHeader about1')),
                ('about2', models.TextField(verbose_name='DetailHeader about2')),
                ('about3', models.TextField(verbose_name='DetailHeader about3')),
                ('about4', models.TextField(verbose_name='DetailHeader about4')),
                ('about5', models.TextField(verbose_name='DetailHeader about5')),
            ],
            options={
                'verbose_name': 'DetailHeader',
                'verbose_name_plural': 'DetailHeaders',
            },
        ),
    ]