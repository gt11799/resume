from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from contact.models import email_list


def resume_index(request):    
    return render_to_response('amazon.html')
    
def check_email(request):
    emails = email_list.objects.all()
    return render_to_response('email_print.html',{'emails':emails})
        
