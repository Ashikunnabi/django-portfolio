# Generated by Django 2.1.4 on 2018-12-25 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_auto_20181225_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='social_links',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.SocialLink'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='index',
            name='description',
            field=models.TextField(max_length=140),
        ),
    ]
