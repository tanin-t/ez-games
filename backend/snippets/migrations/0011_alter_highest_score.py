# Generated by Django 4.2.6 on 2023-11-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0010_remove_highest_input_remove_highest_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highest',
            name='score',
            field=models.JSONField(null=True),
        ),
    ]
