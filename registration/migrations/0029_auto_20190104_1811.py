# Generated by Django 2.1.3 on 2019-01-04 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0028_succesfullregistration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='cgst',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='city',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='country',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='email',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='gstin',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='igst',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='invoice',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='ipa_enrollment_number',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='landline',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='purpose_of_payment',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='sgst',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='state',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='taxable_amount',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='total',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='txn_method',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='txn_status',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='txnid',
        ),
        migrations.RemoveField(
            model_name='succesfullregistration',
            name='txnid_pg',
        ),
        migrations.AddField(
            model_name='succesfullregistration',
            name='registration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='registration.Registration'),
        ),
    ]