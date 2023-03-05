# Generated by Django 4.1.5 on 2023-01-30 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0061_alter_newsletter_about1_alter_newsletter_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailNewsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='DetailNewsletter name')),
                ('name1', models.CharField(max_length=50, verbose_name='DetailNewsletter name1')),
                ('about', models.TextField(verbose_name='DetailNewsletter about')),
                ('about1', models.TextField(verbose_name='DetailNewletter about1')),
                ('img', models.ImageField(upload_to='media', verbose_name='DetailNewsletter image')),
            ],
            options={
                'verbose_name': 'DetailNewsletter',
                'verbose_name_plural': 'DetailNewsletters',
            },
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='about1',
            field=models.TextField(verbose_name='Newsletter about1'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='img',
            field=models.ImageField(null=True, upload_to='media', verbose_name='Newsletter image'),
        ),
    ]