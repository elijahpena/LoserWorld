# Generated by Django 2.2.3 on 2019-07-30 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20190730_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='adult',
            field=models.BooleanField(default=False),
        ),
    ]
