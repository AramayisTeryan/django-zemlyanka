# Generated by Django 4.1.5 on 2023-01-27 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_lunch'),
    ]

    operations = [
        migrations.CreateModel(
            name='LunchImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='LunchImage name')),
                ('name1', models.CharField(max_length=50, verbose_name='LunchImage name1')),
                ('about', models.TextField(verbose_name='LunchImage about')),
                ('about1', models.TextField(blank=True, verbose_name='LunchImage about1')),
                ('about2', models.TextField(verbose_name='LunchImage about2')),
                ('img', models.ImageField(upload_to='media', verbose_name='LunchImage image')),
            ],
        ),
    ]
