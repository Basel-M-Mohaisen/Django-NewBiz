# Generated by Django 3.1.5 on 2021-02-18 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0011_auto_20210216_2225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created_at',)},
        ),
    ]
