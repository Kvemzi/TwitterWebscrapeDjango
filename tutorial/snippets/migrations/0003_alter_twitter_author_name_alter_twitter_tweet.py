# Generated by Django 4.1.3 on 2022-11-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_twitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitter',
            name='author_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='twitter',
            name='tweet',
            field=models.TextField(),
        ),
    ]
