# Generated by Django 4.2.5 on 2023-09-20 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sihpredict', '0004_news_delete_article_delete_receipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='newssource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NewsSource', models.TextField()),
            ],
        ),
    ]
