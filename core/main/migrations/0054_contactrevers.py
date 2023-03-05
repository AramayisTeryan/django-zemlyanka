# Generated by Django 4.1.5 on 2023-01-28 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_updaterevers'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRevers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ContactRevers name')),
                ('name1', models.CharField(max_length=50, verbose_name='ContactRevers name1')),
                ('about', models.TextField(verbose_name='ContactRevers about')),
                ('about1', models.TextField(verbose_name='ContactRevers about1')),
                ('about2', models.TextField(verbose_name='ContactRevers about2')),
                ('about3', models.TextField(verbose_name='ContactRevers about3')),
                ('about4', models.TextField(verbose_name='ContactRevers about4')),
                ('about5', models.TextField(verbose_name='ContactRevers about5')),
                ('about6', models.TextField(verbose_name='ContactRevers about6')),
            ],
            options={
                'verbose_name': 'ContactRevers',
                'verbose_name_plural': 'ConatactReverses',
            },
        ),
    ]