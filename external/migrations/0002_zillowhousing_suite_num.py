# Generated by Django 2.2.6 on 2019-11-04 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('external', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zillowhousing',
            name='suite_num',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
