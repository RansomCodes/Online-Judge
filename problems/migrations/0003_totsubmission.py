# Generated by Django 4.1.9 on 2023-07-20 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_testcases'),
    ]

    operations = [
        migrations.CreateModel(
            name='totsubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('verdict', models.CharField(max_length=100)),
                ('time_of_submission', models.TimeField()),
            ],
        ),
    ]