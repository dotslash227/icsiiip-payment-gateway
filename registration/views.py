from django.shortcuts import render
from django.views import View
from .models import Registration
from .forms import RegistrationForm
from django.utils import timezone
import hashlib
import hmac
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

class IndexPage(View):
    def get(self, request):
        form = RegistrationForm()

        return render(request, "registration/index.html", {
            "form": form,
        })

    def post(self, request):
        form = RegistrationForm(request.POST)
        reg = form.save(commit=False)
        
        if reg.purpose_of_payment == 1:
            reg.amount = 7000
            reg.gst_amount = 1260
        if reg.purpose_of_payment == 2:
            reg.amount = 10000
            reg.gst_amount = 1800
        if reg.purpose_of_payment == 4:
            reg.amount = 1500
            reg.gst_amount = 270

        total_amount = reg.amount + reg.gst_amount
        # total_amount = 1.00

        reg.txnid = "ICSI-IIPAM-%s/%s" % (str(reg.purpose_of_payment), reg.ipa_enrollment_number)
        
        merchant_id = "ICSIIPAM"
        security_id = "icsiipam"
        billdeskurl = "https://pgi.billdesk.com/pgidsk/PGIMerchantPayment"
        ru = "http://onlinepayment.icsiiip.com/handle-payment"
        key = "0BiJitDZQ86Z"

        hash_string_msg = "%s|%s|NA|%s|NA|NA|NA|INR|NA|R|%s|NA|NA|F|%s|%s|NA|NA|NA|NA|NA|%s" % (merchant_id,reg.txn_id, total_amount,security_id,reg.mobile,reg.email,ru)
        hash_string = hash_string_msg.encode("utf-8")
        h = hmac.new(b'0BiJitDZQ86Z', hash_string, hashlib.sha256)
        h = h.hexdigest().upper()

        reg.save()

        msg = "%s|%s" %(hash_string_msg, h)        

        post_data = {"msg":msg}

        return render(request, "registration/confirmation.html", {
            "msg": msg, "reg":reg, "amount":total_amount,
        })


@csrf_exempt
def handle_payment(request):
    msg = request.POST.get("msg")
    msg = msg.split("|")
    status = msg[24]
    mobile = msg[16]
    email = msg[17]

    customer = Registration.objects.filter(email=email).order_by("-pk")[0]
    customer.txn_method = "BillDesk"
    customer.txn_status = "success"
    customer.save()

    return render(request, "registration/success.html", {})