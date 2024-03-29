# Generated by Django 2.1.1 on 2018-11-02 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_registration_gst_mode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='gst_amount',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='gst_mode',
        ),
        migrations.AddField(
            model_name='registration',
            name='cgst',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='igst',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='sgst',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
