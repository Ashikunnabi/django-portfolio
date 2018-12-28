# Generated by Django 2.1.4 on 2018-12-25 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0009_auto_20181225_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index',
            name='social_links',
        ),
        migrations.AddField(
            model_name='sociallink',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.Index'),
            preserve_default=False,
        ),
    ]
