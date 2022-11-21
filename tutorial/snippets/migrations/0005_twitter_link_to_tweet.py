# Generated by Django 4.1.3 on 2022-11-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_twitter_author_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitter',
            name='link_to_tweet',
            field=models.TextField(default='', verbose_name='https://twitter.com/<django.db.models.fields.CharField>/status/<django.db.models.fields.IntegerField>'),
            preserve_default=False,
        ),
    ]
