# Generated by Django 4.1.5 on 2023-01-27 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_dinner'),
    ]

    operations = [
        migrations.CreateModel(
            name='DinnerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='DinnerImage name')),
                ('name1', models.CharField(max_length=50, verbose_name='DinnerImage name1')),
                ('about', models.TextField(verbose_name='DinnerImage about')),
                ('about1', models.TextField(verbose_name='DinnerImage about1')),
                ('img', models.ImageField(upload_to='media', verbose_name='DinnerImage image')),
            ],
            options={
                'verbose_name': 'DinnerImage',
                'verbose_name_plural': 'DinnerImages',
            },
        ),
    ]
