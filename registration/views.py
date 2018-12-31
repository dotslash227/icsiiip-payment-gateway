from django.shortcuts import render
from django.views import View
from .models import Registration, PaymentTypes
from .forms import RegistrationForm
from django.utils import timezone
import hashlib
import hmac
from django.http import HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from weasyprint import HTML
from django.conf import settings
import os

def send_email(customer_details):
    html_content_original = render_to_string("registration/invoice_temp.html", {"customer":customer_details, "msg":"ORIGINAL FOR RECIPIENT"})
    html_content_duplicate = render_to_string("registration/invoice_temp.html", {"customer":customer_details, "msg":"DUPLICATE FOR SUPPLIER"})
    text_content = "Thank you for your payment with ICSI Institute of Insolvency Professionals. Your invoice for the payments made has been attached with this email."
    html_pdf_original = HTML(string=html_content_original)
    html_pdf_duplicate = HTML(string=html_content_duplicate)
    enrollment_number_tem = customer_details.ipa_enrollment_number.replace("/","")  
    path_original = "%s/media-files/invoices/IIP_%s_%s.pdf" % (settings.BASE_DIR,enrollment_number_tem,customer_details.pk)
    path_duplicate = "%s/media-files/invoices/IIP_%s_%s_DUPLICATE.pdf" % (settings.BASE_DIR,enrollment_number_tem,customer_details.pk)
    html_pdf_original.write_pdf(target=path_original)
    html_pdf_duplicate.write_pdf(target=path_duplicate)
    subject = "Your invoice for payments made at ICSI-IIP payment portal"
    from_email = "no-reply@icsi.edu"        
    msg_original = EmailMultiAlternatives(subject, text_content, from_email, [customer_details.email])    
    msg_duplicate = EmailMultiAlternatives(subject, text_content, from_email, ["vikram.taneja@icsi.edu"])    
    msg_original.attach_file(path_original)
    msg_duplicate.attach_file(path_duplicate)

    customer_details.invoice = "/invoices/IIP_%s_%s.pdf" % (enrollment_number_tem, customer_details.pk)
    customer_details.save()

    try:      
        # print ("emailing")              
        msg_original.send()
        msg_duplicate.send()
    except:
        return False
    else:
        return True    

class IndexPage(View):    

    def get(self, request):
        form = RegistrationForm()
        payment_types = PaymentTypes.objects.filter(hidden=False)

        return render(request, "registration/index.html", {
            "form": form, "pt": payment_types,
        })

    def post(self, request):
        form = RegistrationForm(request.POST)
        reg = form.save(commit=False)
        payment_types = PaymentTypes.objects.filter(hidden=False)
        
        total_amount = reg.purpose_of_payment.fees + reg.purpose_of_payment.gst_amount
        reg.total = total_amount
        reg.taxable_amount = reg.purpose_of_payment.fees
        # total_amount = 1.00
        
        reg.save()
        reg.txnid = "IIP/%s-%s/00%s" % (reg.date_added.year%100, (reg.date_added.year%100)+1, reg.pk)
        
        if not reg.gstin:
            if reg.state == "Delhi":                
                flag = False
                reg.cgst = reg.purpose_of_payment.gst_amount/2
                reg.sgst = reg.purpose_of_payment.gst_amount/2
                reg.gstin = "Not Applicable"
            else:
                flag = False
                reg.igst = reg.purpose_of_payment.gst_amount
                reg.gstin = "Not Applicable"
        else:   
            gst_state = reg.gstin[0:2]
            pan_status = reg.gstin[5]
            if pan_status != "P":
                flag = True
            else:
                flag = False
            if gst_state == "07":
                reg.cgst = reg.purpose_of_payment.gst_amount/2
                reg.sgst = reg.purpose_of_payment.gst_amount/2
            else:
                reg.igst = reg.purpose_of_payment.gst_amount
        
        merchant_id = "ICSIIPAM"
        security_id = "icsiipam"
        billdeskurl = "https://pgi.billdesk.com/pgidsk/PGIMerchantPayment"
        ru = "http://onlinepayment.icsiiip.com/handle-payment"
        # ru = "http://127.0.0.1:8000/handle-payment"
        key = "0BiJitDZQ86Z"

        hash_string_msg = "%s|%s|NA|%s|NA|NA|NA|INR|NA|R|%s|NA|NA|F|%s|%s|NA|NA|NA|NA|NA|%s" % (merchant_id,reg.txnid, total_amount,security_id,reg.mobile,reg.email,ru)
        hash_string = hash_string_msg.encode("utf-8")
        h = hmac.new(b'0BiJitDZQ86Z', hash_string, hashlib.sha256)
        h = h.hexdigest().upper()

        reg.save()
        # Invoice format ICSIIIPMA/year/month/pk
        reg.txnid = "IIP/%s-%s/00%s" % (reg.date_added.year%100, (reg.date_added.year%100)+1, reg.pk)

        reg.save()        

        msg = "%s|%s" %(hash_string_msg, h)        

        # post_data = {"msg":msg}        

        if flag:
            return render(request, "registration/index.html", {
                "form": form, "error":"Please enter an individual's GST Number to claim input.",
                "pt": payment_types
            })
        else:
            # send_email(reg)                 
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