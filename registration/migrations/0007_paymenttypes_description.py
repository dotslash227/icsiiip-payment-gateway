# Generated by Django 2.1.1 on 2018-10-31 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20181031_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenttypes',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
