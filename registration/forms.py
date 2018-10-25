from django import forms
from django.forms import ModelForm
from .models import Registration

class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        exclude = ["txn_status", "txnid", "txn_method", "date_added", "amount", "gst_amount", "txnid_pg"]