# Generated by Django 4.1.5 on 2023-01-30 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0060_detailnewimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='about1',
            field=models.TextField(verbose_name='Newletter about1'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='img',
            field=models.ImageField(upload_to='media', verbose_name='Newsletter image'),
        ),
    ]
