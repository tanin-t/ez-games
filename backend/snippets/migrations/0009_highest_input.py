# Generated by Django 4.2.6 on 2023-11-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_alter_snippet_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='highest',
            name='input',
            field=models.BooleanField(default=False),
        ),
    ]
