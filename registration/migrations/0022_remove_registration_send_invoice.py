# Generated by Django 2.1.3 on 2018-11-13 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0021_registration_send_invoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='send_invoice',
        ),
    ]
