from django.shortcuts import render, redirect

from apps.user.models import User
from apps.common.models import SubEmail


def about(request):
    url = request.META.get('HTTP_REFERER')

    user = User.objects.get(id=1)

    if request.method == "POST":
        email = request.POST.get("subemail")
        
        SubEmail.objects.create(
            email=email,
        )

        return redirect(url)

    return render(request, 'about.html', {"user": user})