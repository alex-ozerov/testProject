from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from testTask.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL

def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            password = form.cleaned_data['password']
            try:
                send_mail("Sign Up", f'name: {name}, from_email: {from_email}, password: {password}',DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('error')
            return redirect('success')
    else:
        return HttpResponse('error')
    return render(request, "home.html", {'form': form})

def success_view(request):
    return HttpResponse('Cool!')
