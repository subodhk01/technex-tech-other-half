# Generated by Django 3.0.2 on 2020-02-03 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200202_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='qno',
            field=models.IntegerField(null=True),
        ),
    ]
