# Generated by Django 2.1.4 on 2018-12-28 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0004_programminglanguageicons_workflow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programminglanguageicons',
            name='icon',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='workflow',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]