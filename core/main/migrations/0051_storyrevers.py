# Generated by Django 4.1.5 on 2023-01-28 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_homerevers'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryRevers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='StoryRevers name')),
                ('name1', models.CharField(max_length=50, verbose_name='StoryRevers name1')),
                ('about', models.TextField(verbose_name='StoryRevers about')),
                ('about1', models.TextField(verbose_name='StoryRevers about1')),
                ('about2', models.TextField(verbose_name='StoryRevers about2')),
                ('about3', models.TextField(verbose_name='StoryRevers about3')),
                ('about4', models.TextField(verbose_name='StoryRevers about4')),
                ('about5', models.TextField(verbose_name='StoryRevers about5')),
                ('about6', models.TextField(verbose_name='StoryRevers about6')),
            ],
            options={
                'verbose_name': 'StoryRevers',
                'verbose_name_plural': 'StoryReverses',
            },
        ),
    ]