from django.db import models
from django.utils import timezone


class PaymentTypes(models.Model):
    name = models.CharField(max_length=150)
    shortcode = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    fees = models.FloatField(default=0.00)
    gst_amount = models.FloatField(default=0.00)

    def __str__(self):
        return self.name


class Registration(models.Model):
    date_added = models.DateField(default=timezone.now)
    ipa_enrollment_number = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(max_length=150)
    gstin = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.BigIntegerField()
    address1 = models.CharField(max_length=150, verbose_name="Address Line 1")
    address2 = models.CharField(max_length=150, verbose_name="Address Line 2", blank=True, null=True)
    landline = models.BigIntegerField(blank=True, null=True)
    country = models.CharField(max_length=150, default="India")    
    purpose_of_payment = models.ForeignKey(PaymentTypes, blank=True, null=True, on_delete=models.CASCADE)
    txn_status = models.CharField(max_length=50, blank=True, null=True)
    txnid = models.CharField(max_length=50, blank=True, null=True)
    txnid_pg = models.CharField(max_length=50, blank=True, null=True)
    txn_method = models.CharField(max_length=50, blank=True, null=True)
    amount = models.FloatField(default=0.00)
    gst_amount = models.FloatField(default=0.00)
    gst_mode = models.IntegerField(default=1, choices=(
        (1, "CGST/SGST"),
        (2, "IGST")
    ))

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)