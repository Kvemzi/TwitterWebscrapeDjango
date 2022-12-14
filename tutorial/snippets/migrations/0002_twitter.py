# Generated by Django 4.1.3 on 2022-11-16 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Twitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.IntegerField()),
                ('tweet_id', models.IntegerField()),
                ('tweet', models.CharField(default='', max_length=1000)),
                ('created_at', models.DateTimeField()),
                ('author_name', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
