# Generated by Django 2.1.1 on 2018-11-06 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_auto_20181106_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
