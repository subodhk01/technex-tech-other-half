# Generated by Django 3.0.2 on 2020-02-05 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_question_qtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='label',
            field=models.TextField(blank=True),
        ),
    ]
