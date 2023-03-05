# Generated by Django 4.1.5 on 2023-01-26 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_breakfast'),
    ]

    operations = [
        migrations.CreateModel(
            name='BreakfastImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='BreakfastImage name')),
                ('name1', models.CharField(max_length=30, verbose_name='BreakfastImage name1')),
                ('about', models.TextField(verbose_name='BreakfastImage about')),
                ('about1', models.TextField(verbose_name='BreakfastImage about1')),
            ],
            options={
                'verbose_name': 'BreakfastImage',
                'verbose_name_plural': 'BreakfastImages',
            },
        ),
    ]
