from django.shortcuts import render
from django.views import View
from .models import Registration, PaymentTypes
from .forms import RegistrationForm
from django.utils import timezone
import hashlib
import hmac
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email(customer_details):
    gst_half = customer_details.gst_amount/2
    subject = "Your invoice for payments made at ICSI-IIP payment portal"
    from_email = "no-reply@icsi.edu"
    html_content = render_to_string("registration/invoice.html", {"customer":customer_details, "gst_half":gst_half})
    text_content = strip_tags(html_content)

    print (html_content)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [customer_details.email])
    msg.attach_alternative(html_content, "text/html")

    try:
        msg.send()
    except:
        return False
    else:
        return True    

class IndexPage(View):
    def get(self, request):
        form = RegistrationForm()
        payment_types = PaymentTypes.objects.all()

        return render(request, "registration/index.html", {
            "form": form, "pt": payment_types,
        })

    def post(self, request):
        form = RegistrationForm(request.POST)
        reg = form.save(commit=False)
        payment_types = PaymentTypes.objects.all()
        
        total_amount = reg.purpose_of_payment.fees + reg.purpose_of_payment.gst_amount
        # total_amount = 1.00

        reg.txnid = "ICSI-IIPAM-%s/%s" % (str(reg.purpose_of_payment.shortcode), reg.ipa_enrollment_number)
        
        if not reg.gstin:
            flag = False
        else:
            gst_state = reg.gstin[0:2]
            pan_status = reg.gstin[5]
            if pan_status != "P":
                flag = True
            else:
                flag = False
            if gst_state == "07":
                reg.gst_mode = 1
            else:
                reg.gst_mode = 2
        
        merchant_id = "ICSIIPAM"
        security_id = "icsiipam"
        billdeskurl = "https://pgi.billdesk.com/pgidsk/PGIMerchantPayment"
        ru = "http://onlinepayment.icsiiip.com/handle-payment"
        key = "0BiJitDZQ86Z"

        hash_string_msg = "%s|%s|NA|%s|NA|NA|NA|INR|NA|R|%s|NA|NA|F|%s|%s|NA|NA|NA|NA|NA|%s" % (merchant_id,reg.txnid, total_amount,security_id,reg.mobile,reg.email,ru)
        hash_string = hash_string_msg.encode("utf-8")
        h = hmac.new(b'0BiJitDZQ86Z', hash_string, hashlib.sha256)
        h = h.hexdigest().upper()

        reg.save()

        msg = "%s|%s" %(hash_string_msg, h)        

        post_data = {"msg":msg}

        if flag:
            return render(request, "registration/index.html", {
                "form": form, "error":"Please enter an individual's GST Number to claim input.",
                "pt": payment_types
            })
        else:
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
    txnid_pg = msg[2]

    customer = Registration.objects.filter(email=email).order_by("-pk")[0]

    customer.txn_method = "BillDesk"
    customer.txn_status = status
    customer.txnid_pg = txnid_pg
    customer.save()

    msg = send_email(customer)
    if msg:
        print ("email succesfull")
    else:
        print ("email not succesfull")

    return render(request, "registration/success.html", {})