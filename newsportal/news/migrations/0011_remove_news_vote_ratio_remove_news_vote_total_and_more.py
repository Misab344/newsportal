# Generated by Django 4.0.3 on 2022-03-24 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_remove_news_tags_delete_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='vote_ratio',
        ),
        migrations.RemoveField(
            model_name='news',
            name='vote_total',
        ),
        migrations.RemoveField(
            model_name='review',
            name='project',
        ),
        migrations.RemoveField(
            model_name='review',
            name='value',
        ),
        migrations.AddField(
            model_name='news',
            name='verified_news',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='news',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.news'),
        ),
        migrations.AlterField(
            model_name='news',
            name='featured_image',
            field=models.ImageField(blank=True, default='news/default.jpg', null=True, upload_to='news/'),
        ),
    ]
