# Generated by Django 5.1.3 on 2024-11-14 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_yeardate',
            field=models.IntegerField(),
        ),
    ]
