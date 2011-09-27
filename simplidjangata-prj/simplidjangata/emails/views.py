# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.forms.models import ModelForm
from models import Email
from django.template.context import RequestContext
from django.core.mail import send_mail
import sys

# to be moved out on different file
class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields=('recipient', 'subject', 'text')

def index(request):
    return HttpResponse("we are going to send an Email to somebody")

def prepare(request):
    if request.method == 'POST': # If the form has been submitted...
        form = EmailForm(request.POST) # A form bound to the POST data 
        if form.is_valid(): # All validation rules pass

            emailModel = form.save(commit=False)
            emailModel.originator = 'giubeppe@localhost'        
            emailModel.save()
            
            try:
                send_mail(emailModel.subject, emailModel.text, emailModel.originator, [emailModel.recipient])
            except:
                print "Error sending email:", sys.exc_info()[0]

            return HttpResponse("thanks for filling the form ")
    else:
        form = EmailForm()
        
    return render_to_response('emails/prepare.html', {'form': form}, 
                              context_instance=RequestContext(request))
