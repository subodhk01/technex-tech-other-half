# Generated by Django 3.0.2 on 2020-02-01 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200201_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='qid',
            field=models.CharField(default='ques', max_length=10),
            preserve_default=False,
        ),
    ]
