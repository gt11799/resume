# _*_coding=utf8 _*_
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from forms import ContactForm
from models import email_list

def contact(request):
    
    errors = []
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            email_message = cd.get('email', 'No email') + u'\n' + cd.get('subject', 'no subject') + u'\n' + cd.get('message','No message')
            
            db = email_list(
                email = cd.get('email', 'No email'),
                content = email_message
            )
            db.save()
            
            send_mail(
                cd['subject'],
                email_message,
                'gongting88@yeah.net',
                ['gting405@163.com'],
                fail_silently=True,
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject':u'网站还可以哦'})
    return render_to_response('contact_form.html', {'form': form})
    
def thanks(request):
    return render_to_response('thanks.html')
