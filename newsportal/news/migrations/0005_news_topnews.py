# Generated by Django 4.0 on 2021-12-26 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_category_id_alter_topnews_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='topNews',
            field=models.ManyToManyField(blank=True, to='news.TopNews'),
        ),
    ]
