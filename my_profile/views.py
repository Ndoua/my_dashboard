from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import ContactForm
from django.http import HttpResponse


def profile(request):

    return render(request, 'my_profile/index.html')


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            messages.success(request, f'Message reçu, je vous repond dès que possible, bye')
            try:
                send_mail(subject, message, from_email, ['serge.ndoua@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('profile')
    return render(request, "my_profile/contact.html", {'form': form})


def contact_success(request):
    return render(request, 'my_profile/index.html')

