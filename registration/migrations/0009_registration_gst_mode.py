# Generated by Django 2.1.1 on 2018-10-31 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_paymenttypes_shortcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='gst_mode',
            field=models.IntegerField(choices=[(1, 'CGST/SGST'), (2, 'IGST')], default=1),
        ),
    ]
