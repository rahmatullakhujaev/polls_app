# Generated by Django 5.0.1 on 2024-01-31 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
