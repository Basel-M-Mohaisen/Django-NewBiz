# Generated by Django 3.1.5 on 2021-02-23 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0003_auto_20210223_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(),
        ),
    ]
