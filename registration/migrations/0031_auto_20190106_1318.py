# Generated by Django 2.1.3 on 2019-01-06 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0030_succesfullregistration_invoice_series'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='registration',
        ),
        migrations.DeleteModel(
            name='SuccesfullRegistration',
        ),
    ]
