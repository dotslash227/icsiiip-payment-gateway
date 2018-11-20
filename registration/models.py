from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("Delhi","Delhi"),("Puducherry","Puducherry"))



class PaymentTypes(models.Model):
    name = models.CharField(max_length=150)
    hsnsac = models.CharField(max_length=150, default="None", blank=True, null=True)
    shortcode = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    fees = models.FloatField(default=0.00)
    gst_amount = models.FloatField(default=0.00)
    hidden = models.BooleanField(default=False, choices=(
        (True, "Yes"),
        (False, "No")
    ))

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
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25, choices=state_choices, default="Delhi")
    pincode = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=150, default="India")    
    landline = models.BigIntegerField(blank=True, null=True)    
    purpose_of_payment = models.ForeignKey(PaymentTypes, blank=True, null=True, on_delete=models.CASCADE)
    txn_status = models.CharField(max_length=50, blank=True, null=True)
    txnid = models.CharField(max_length=50, blank=True, null=True)
    txnid_pg = models.CharField(max_length=50, blank=True, null=True)
    txn_method = models.CharField(max_length=50, blank=True, null=True, choices=(
        ("BillDesk", "BillDesk"),
        ("Cash", "Cash"),
        ("NEFT/IMPS/RTGS", "NEFT/IMPS/RTGS"),
        ("Cheque", "Cheque"),
    ))
    amount = models.FloatField(default=0.00)
    igst = models.FloatField(blank=True, null=True)
    cgst = models.FloatField(blank=True, null=True)
    sgst = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    invoice = models.FileField(max_length=150, upload_to="invoices", blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        super(Registration, self).save(*args, **kwargs)
        self.txnid = "ICSIIIP/%s-%s/00%s" % (self.date_added.year%100, (self.date_added.year%100)+1, self.pk)        
        super(Registration, self).save(*args, **kwargs)