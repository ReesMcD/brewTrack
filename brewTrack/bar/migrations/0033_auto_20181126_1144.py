# Generated by Django 2.1.2 on 2018-11-26 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0032_auto_20181126_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bar',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(default='None Menu', max_length=100),
        ),
    ]
