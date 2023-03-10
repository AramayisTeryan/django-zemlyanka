# Generated by Django 4.1.5 on 2023-01-28 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0051_storyrevers'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuRevers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='MenuRevers name')),
                ('name1', models.CharField(max_length=50, verbose_name='MenuRevers name1')),
                ('about', models.TextField(verbose_name='MenuRevers about')),
                ('about1', models.TextField(verbose_name='MenuRevers about1')),
                ('about2', models.TextField(verbose_name='MenuRevers about2')),
                ('about3', models.TextField(verbose_name='MenuRevers about3')),
                ('about4', models.TextField(verbose_name='MenuRevers about4')),
                ('about5', models.TextField(verbose_name='MenuRevers about5')),
                ('about6', models.TextField(verbose_name='MenuRevers about6')),
            ],
            options={
                'verbose_name': 'MenuRevers',
                'verbose_name_plural': 'MenuReverses',
            },
        ),
    ]
