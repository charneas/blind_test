# Generated by Django 5.1.3 on 2024-11-14 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=200)),
                ('song_yeardate', models.DateField(verbose_name='date published')),
                ('song_writer', models.CharField(max_length=200)),
                ('song_origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.country')),
            ],
        ),
    ]
