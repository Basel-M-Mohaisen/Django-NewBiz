# Generated by Django 3.1.5 on 2021-02-15 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learn',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='learn',
            name='purport',
            field=models.TextField(),
        ),
    ]