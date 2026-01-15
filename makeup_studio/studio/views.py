from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm
from .models import ContactMessage
from django.conf import settings


# Homepage
def home(request):
    return render(request, 'studio/home.html')

# Services page
def services(request):
    return render(request, 'studio/services.html')

# Portfolio page
def portfolio(request):
    return render(request, 'studio/portfolio.html')

def gallery(request):
    return render(request, 'studio/gallery.html')

def transformations(request):
    return render(request, 'studio/transformations.html')

# Contact page
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            contact_msg = ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
            )

            # Send email notification
            subject = f"New Contact Form Submission from {contact_msg.name}"
            body = f"Name: {contact_msg.name}\nEmail: {contact_msg.email}\nPhone: {contact_msg.phone}\n\nMessage:\n{contact_msg.message}"
            
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,  # from email
                ['Your_Email'],      # recipient email (can be same as sender)
                fail_silently=False,
            )

            messages.success(request, 'Thank you! Your message has been saved and email sent.')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'studio/contact.html', {'form': form})


