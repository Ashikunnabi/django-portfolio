# Generated by Django 2.1.4 on 2018-12-26 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0016_project_sub_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='site_link_icon',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
