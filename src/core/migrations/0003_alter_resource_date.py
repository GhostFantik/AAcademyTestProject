# Generated by Django 3.2 on 2021-04-15 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_resources_resource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='date',
            field=models.DateField(verbose_name='Дата последнего поступления'),
        ),
    ]
