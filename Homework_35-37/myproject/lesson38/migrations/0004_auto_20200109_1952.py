# Generated by Django 2.2 on 2020-01-09 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson38', '0003_auto_20200109_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
    ]
