# Generated by Django 3.1 on 2021-04-19 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitedplace',
            name='place',
            field=models.CharField(max_length=40, null=True),
        ),
    ]