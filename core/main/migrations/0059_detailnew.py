# Generated by Django 4.1.5 on 2023-01-28 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0058_detailcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='DetailNew name')),
            ],
            options={
                'verbose_name': 'DetailNew',
                'verbose_name_plural': 'DetailNews',
            },
        ),
    ]
