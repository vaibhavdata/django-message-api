# Generated by Django 3.2.5 on 2022-06-29 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]