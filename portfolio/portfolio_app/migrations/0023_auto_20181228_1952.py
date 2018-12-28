# Generated by Django 2.1.4 on 2018-12-28 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0022_auto_20181228_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('file', models.FileField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.Index')),
            ],
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact page'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Others message'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='sub_title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]