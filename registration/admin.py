from django.contrib import admin

from .models import Registration

class RegisterAdmin(admin.ModelAdmin):
    list_display = ["first_name", "middle_name", "last_name", "email", "ipa_enrollment_number", "gstin", "mobile", "purpose_of_payment"]
    search_fields = ["first_name", "last_name", "email", "mobile", "ipa_enrollment_number", "gstin", "purpose_of_payment"]
    list_filter = ["purpose_of_payment"]

admin.site.register(Registration, RegisterAdmin)