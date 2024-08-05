from django.shortcuts import render, redirect

from apps.common.models import SubEmail
from apps.blog.models import Blog


def blog(request):
    url = request.META.get('HTTP_REFERER')

    blogs = Blog.objects.all().order_by("id")[:4]

    if request.method == "POST":
        email = request.POST.get("subemail")
        
        SubEmail.objects.create(
            email=email,
        )

        return redirect(url)

    return render(request, 'blog.html', {"blogs": blogs})
