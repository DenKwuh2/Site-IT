# Generated by Django 4.0.3 on 2022-03-17 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='view',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='Категории'),
        ),
    ]
