# Generated by Django 4.1.5 on 2023-01-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0055_detailheader'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='DetailHead name')),
            ],
            options={
                'verbose_name': 'DetailHead',
                'verbose_name_plural': 'DetailHeads',
            },
        ),
    ]
