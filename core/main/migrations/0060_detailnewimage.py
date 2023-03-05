# Generated by Django 4.1.5 on 2023-01-28 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0059_detailnew'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailNewImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='DetailNewImage name')),
                ('about', models.TextField(null=True, verbose_name='DetailNewImage about')),
                ('about1', models.TextField(null=True, verbose_name='DetailNewImage about1')),
                ('img', models.ImageField(null=True, upload_to='media', verbose_name='DetailNewImage image')),
            ],
            options={
                'verbose_name': 'DetailNewImage',
                'verbose_name_plural': 'DetailNewImages',
            },
        ),
    ]
