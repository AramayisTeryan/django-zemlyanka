# Generated by Django 4.1.5 on 2023-01-30 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0062_detailnewsletter_alter_newsletter_about1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailFoot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='DetailFoot name')),
                ('name1', models.CharField(max_length=50, verbose_name='DetailFoot name1')),
                ('name2', models.CharField(max_length=50, verbose_name='DetailFoot name2')),
                ('name3', models.CharField(max_length=50, verbose_name='DetailFoot name3')),
                ('name4', models.CharField(max_length=50, verbose_name='DetailFoot name4')),
                ('about', models.TextField(verbose_name='DetailFoot about')),
                ('about1', models.TextField(verbose_name='DetailFoot about1')),
                ('about2', models.TextField(verbose_name='DetailFoot about2')),
                ('about3', models.TextField(verbose_name='DetailFoot about3')),
                ('about4', models.TextField(verbose_name='DetailFoot about4')),
            ],
            options={
                'verbose_name': 'DetailFoot',
                'verbose_name_plural': 'DetailFoots',
            },
        ),
    ]
