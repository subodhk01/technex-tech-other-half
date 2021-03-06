# Generated by Django 3.0.2 on 2020-02-03 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20200203_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomEntry',
            fields=[
                ('technexid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('ques1', models.CharField(max_length=70)),
                ('ques2', models.CharField(max_length=70)),
                ('ques3', models.CharField(max_length=70)),
                ('ques4', models.CharField(max_length=70)),
                ('ques5', models.CharField(max_length=70)),
                ('ques6', models.CharField(max_length=70)),
                ('ques7', models.CharField(max_length=70)),
                ('ques8', models.CharField(max_length=70)),
                ('ques9', models.CharField(max_length=70)),
                ('ques10', models.CharField(max_length=70)),
                ('ques11', models.CharField(max_length=70)),
                ('ques12', models.CharField(max_length=70)),
                ('ques13', models.CharField(max_length=70)),
                ('ques14', models.CharField(max_length=70)),
                ('ques15', models.CharField(max_length=70)),
                ('submitted', models.BooleanField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='ques10',
            field=models.CharField(default=None, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='ques11',
            field=models.CharField(default=None, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='ques12',
            field=models.CharField(default=None, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='ques13',
            field=models.CharField(default=None, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='ques14',
            field=models.CharField(default=None, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='ques15',
            field=models.CharField(default=None, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='ques3',
            field=models.CharField(default=None, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='ques4',
            field=models.CharField(default=None, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='ques5',
            field=models.CharField(default=None, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='ques6',
            field=models.CharField(default=None, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='ques7',
            field=models.CharField(default=None, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='ques8',
            field=models.CharField(default=None, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='ques9',
            field=models.CharField(default=None, max_length=70),
            preserve_default=False,
        ),
    ]
