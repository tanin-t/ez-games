# Generated by Django 4.2.6 on 2023-11-03 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0013_alter_highest_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highest',
            name='score',
            field=models.JSONField(default=list, null=True),
        ),
    ]
