# Generated by Django 2.2 on 2019-12-23 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='text',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='comments',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
