# Generated by Django 4.1.5 on 2023-01-28 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0057_detailbody'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='DetailComment name')),
                ('name1', models.CharField(max_length=50, verbose_name='DetailComment name1')),
                ('name2', models.CharField(max_length=50, verbose_name='DetailComment name2')),
                ('name3', models.CharField(max_length=50, verbose_name='DetailComment name3')),
                ('about', models.TextField(verbose_name='DetailComment about')),
                ('about1', models.TextField(verbose_name='DetailComment about1')),
                ('about2', models.TextField(verbose_name='DetailComment about2')),
                ('about3', models.TextField(verbose_name='DetailComment about3')),
                ('img', models.ImageField(upload_to='media', verbose_name='DetailComment image')),
                ('img1', models.ImageField(upload_to='media', verbose_name='DetailComment image1')),
            ],
            options={
                'verbose_name': 'DetailComment',
                'verbose_name_plural': 'DetailComments',
            },
        ),
    ]
