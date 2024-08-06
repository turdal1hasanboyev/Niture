from django.shortcuts import render, redirect

from apps.common.models import SubEmail
from apps.contact.models import Contact


def contact(request):
    url = request.META.get('HTTP_REFERER')

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message,
        )

        return redirect(url)
    
    if request.method == "POST":
        email = request.POST.get("subemail")
        
        SubEmail.objects.create(
            email=email,
        )

        return redirect(url)

    return render(request, 'contact.html')
    