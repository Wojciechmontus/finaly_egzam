from django.shortcuts import render,redirect
from sendmail.form import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_Email']
            message = form.cleaned_data['message']
            try:
                mensaje = "DE: " + from_email + "\n" + message
                send_mail(subject,mensaje,['wojciechmonte@gmail.com'],['wojciechmonte@gmail.com'],fail_silently=False,)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('Correcto')
    return render(request,'sendmail/email.html',{'form':form})

def successView(request):
    return render(request,'sendmail/success.html')


