# Generated by Django 4.1.5 on 2023-01-24 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_headcarusel'),
    ]

    operations = [
        migrations.AddField(
            model_name='headcarusel',
            name='img',
            field=models.ImageField(null=True, upload_to='media', verbose_name='HeadCarusel image'),
        ),
    ]
