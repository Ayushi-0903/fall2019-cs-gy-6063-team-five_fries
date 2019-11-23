# Generated by Django 2.2.7 on 2019-11-21 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('external', '0004_delete_zillowhousing'),
    ]

    operations = [
        migrations.CreateModel(
            name='CachedSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_string', models.CharField(db_index=True, max_length=255)),
                ('street', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('zipcode', models.CharField(blank=True, max_length=10)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
    ]