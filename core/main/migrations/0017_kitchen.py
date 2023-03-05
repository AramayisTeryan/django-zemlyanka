# Generated by Django 4.1.5 on 2023-01-26 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_storyheader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Kitchen name')),
                ('about', models.TextField(verbose_name='Kitchen about')),
            ],
            options={
                'verbose_name': 'Kitchen',
                'verbose_name_plural': 'Kitchens',
            },
        ),
    ]
