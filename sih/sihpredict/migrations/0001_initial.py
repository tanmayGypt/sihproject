# Generated by Django 4.2.5 on 2023-09-20 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reciepe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('content', models.TextField()),
                ('urls', models.TextField()),
                ('source', models.TextField()),
            ],
        ),
    ]
