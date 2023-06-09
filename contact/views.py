from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm


def contact_view(request):

    """
    a view to display the contactform
    and handle form submission
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Your message has been sent!')
            return render(request, 'contact/success.html')


        else:
            form = ContactForm()
            messages.warning(request, 'Message not sent. Please try again.')

    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            form = ContactForm()

    form = ContactForm()
    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)