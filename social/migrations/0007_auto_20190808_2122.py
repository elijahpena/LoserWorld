# Generated by Django 2.2.3 on 2019-08-08 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_auto_20190808_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, upload_to='%Y/%m/%d'),
        ),
    ]
