# Generated by Django 2.1.2 on 2018-11-26 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0031_auto_20181126_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='frequancy',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='Frequancy'),
        ),
    ]
