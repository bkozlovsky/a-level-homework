# Generated by Django 2.2 on 2020-01-09 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson38', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=2),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=2),
        ),
    ]