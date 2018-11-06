from django.contrib import admin

from .models import Registration, PaymentTypes
from import_export.admin import ImportExportActionModelAdmin

class RegisterAdmin(ImportExportActionModelAdmin):
    list_display = ["first_name", "middle_name", "last_name", "email", "id", "txnid", "ipa_enrollment_number", "gstin", "mobile", "purpose_of_payment","cgst", "sgst", "igst"]
    search_fields = ["first_name", "last_name", "email", "mobile", "ipa_enrollment_number", "gstin", "purpose_of_payment", "city", "state"]
    list_filter = ["purpose_of_payment", "state"]

admin.site.register(Registration, RegisterAdmin)
admin.site.register(PaymentTypes)