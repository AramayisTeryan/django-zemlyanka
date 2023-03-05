# Generated by Django 4.1.5 on 2023-01-26 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_homefoot'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='StoryHeader name')),
                ('about', models.TextField(verbose_name='StoryHeader about')),
                ('about1', models.TextField(verbose_name='StoryHeader about')),
                ('about2', models.TextField(verbose_name='StoryHeader about')),
                ('about3', models.TextField(verbose_name='StoryHeader about')),
                ('about4', models.TextField(verbose_name='StoryHeader about')),
                ('about5', models.TextField(verbose_name='StoryHeader about')),
            ],
            options={
                'verbose_name': 'StoryHeader',
                'verbose_name_plural': 'StoryHeaders',
            },
        ),
    ]
