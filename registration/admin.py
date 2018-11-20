from django.contrib import admin

from .models import Registration, PaymentTypes
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class RegistrationResource(resources.ModelResource):
    class Meta:
        model = Registration
        fields = ("date_added", "first_name", "middle_name""last_name", "email", "mobile", "gstin", "address1", "address2", "city", "state", "pincode", "purpose_of_payment__name", "txn_status", "txnid", "txnid_pg","txn_methid","amount", "igst","sgst","cgst", "total")

class RegisterAdmin(ImportExportModelAdmin):
    resource_class = RegistrationResource
    list_display = ["first_name", "last_name", "email", "txnid", "state", "ipa_enrollment_number", "gstin", "purpose_of_payment", "cgst", "sgst", "igst", "total", "invoice"]
    search_fields = ["first_name", "last_name", "email", "mobile", "ipa_enrollment_number", "gstin", "purpose_of_payment", "city", "state"]
    list_filter = ["purpose_of_payment", "state"]

admin.site.register(Registration, RegisterAdmin)
admin.site.register(PaymentTypes)