from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from realestateSite import settings
from django.core.mail import send_mail, BadHeaderError


from .forms import ContactForm
from .models import *


def index(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'New Property Consultation'
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phoneNumber = request.POST.get('phoneNumber', '')
            address = request.POST.get('address', '')
            city = request.POST.get('city', '')
            zipCode = request.POST.get('zipCode', '')
            clientInfo = 'Client information: '
            keyFields = [ clientInfo, name, email, phoneNumber, address, city, zipCode ]
            body = '\n'.join(keyFields)
            try:
                send_mail(subject, body, email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "home.html", {'form': form})


def success(request):
    title = {
        'title':"Sell Your House Today!",
        }
    return render(request,'success.html',title)
