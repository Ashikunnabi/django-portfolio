# Generated by Django 2.1.4 on 2019-01-01 07:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0030_auto_20190101_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(max_length=100, validators=[django.core.validators.EmailValidator]),
        ),
    ]