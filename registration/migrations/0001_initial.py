# Generated by Django 2.1.1 on 2018-09-26 04:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('ipa_enrollment_number', models.CharField(max_length=150)),
                ('first_name', models.CharField(max_length=150)),
                ('middle_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('gstin', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.BigIntegerField()),
                ('address1', models.CharField(max_length=150, verbose_name='Address Line 1')),
                ('address2', models.CharField(max_length=150, verbose_name='Address Line 2')),
                ('landline', models.BigIntegerField(blank=True, null=True)),
                ('country', models.CharField(default='India', max_length=150)),
                ('purpose_of_payment', models.IntegerField(choices=[(1, 'Enrollment Fee'), (2, 'Annual Membership Fee'), (3, 'Pre-registration Educational Course Fee Batch 7, Mumbai'), (4, 'Complaints/Greviences')])),
            ],
        ),
    ]
