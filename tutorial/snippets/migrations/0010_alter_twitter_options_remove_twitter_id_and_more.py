# Generated by Django 4.1.3 on 2022-11-23 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0009_delete_snippet'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='twitter',
            options={'ordering': ['created_at']},
        ),
        migrations.RemoveField(
            model_name='twitter',
            name='id',
        ),
        migrations.AlterField(
            model_name='twitter',
            name='tweet_id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
