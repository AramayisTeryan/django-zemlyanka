# Generated by Django 4.1.5 on 2023-01-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_teamimage_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Newsletter name')),
                ('name1', models.CharField(max_length=50, verbose_name='Newsletter name1')),
                ('about', models.TextField(verbose_name='Newsletter about')),
                ('about1', models.TextField(verbose_name='Newsletter about1')),
            ],
            options={
                'verbose_name': 'Newsletter',
                'verbose_name_plural': 'Newsletters',
            },
        ),
    ]