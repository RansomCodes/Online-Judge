# Generated by Django 4.1.9 on 2023-07-20 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_totsubmission_problem'),
    ]

    operations = [
        migrations.AddField(
            model_name='totsubmission',
            name='language',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]