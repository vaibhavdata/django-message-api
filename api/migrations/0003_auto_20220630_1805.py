# Generated by Django 3.2.5 on 2022-06-30 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220629_0713'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['first_name']},
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together={('email', 'first_name')},
        ),
    ]