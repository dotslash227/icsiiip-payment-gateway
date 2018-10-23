from django.db import models
from django.utils import timezone


class Registration(models.Model):
    date_added = models.DateField(default=timezone.now)
    ipa_enrollment_number = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    gstin = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.BigIntegerField()
    address1 = models.CharField(max_length=150, verbose_name="Address Line 1")
    address2 = models.CharField(max_length=150, verbose_name="Address Line 2")
    landline = models.BigIntegerField(blank=True, null=True)
    country = models.CharField(max_length=150, default="India")    
    purpose_of_payment = models.IntegerField(choices=(
        (1, "Enrollment Fee"),
        (2, "Annual Membership Fee"),
        (3, "Pre-registration Educational Course Fee Batch 7, Mumbai"),
        (4, "Complaints/Greviences"),
    ))
    txn_status = models.CharField(max_length=50, blank=True, null=True)
    txnid = models.CharField(max_length=50, blank=True, null=True)
    txn_method = models.CharField(max_length=50, blank=True, null=True)
    amount = models.FloatField(default=0.00)
    gst_amount = models.FloatField(default=0.00)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)