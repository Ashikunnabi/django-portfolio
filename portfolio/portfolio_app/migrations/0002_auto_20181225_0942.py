# Generated by Django 2.1.4 on 2018-12-25 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
