# Generated by Django 3.1.5 on 2021-02-24 20:34

import Account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_auto_20210224_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default=Account.models.default_place_pics, null=True, upload_to='profile/'),
        ),
    ]
