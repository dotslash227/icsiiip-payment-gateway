from django import forms
from django.forms import ModelForm
from .models import Registration, PaymentTypes

class RegistrationForm(ModelForm):
    purpose_of_payment = forms.ModelChoiceField(queryset=PaymentTypes.objects.filter(hidden=False))

    class Meta:
        model = Registration
        exclude = ["txn_status", "txnid", "txn_method", "date_added", "taxable_amount", "gst_amount", "txnid_pg", "igst", "cgst", "sgst", "send_invoice", "invoice", "total"]