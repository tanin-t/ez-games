# Generated by Django 4.2.6 on 2023-10-31 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_highest'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='answer',
            field=models.IntegerField(default=1),
        ),
    ]
