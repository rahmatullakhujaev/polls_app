# Generated by Django 5.0.1 on 2024-01-31 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_answers_votes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answers',
            old_name='question_id',
            new_name='question',
        ),
    ]
