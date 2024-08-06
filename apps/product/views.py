from django.shortcuts import render, redirect

from apps.common.models import SubEmail
from apps.product.models import Category, Product, Banner, Review
from apps.contact.models import Contact


def home(request):
    url = request.META.get('HTTP_REFERER')

    catogories = Category.objects.filter(is_active=True).order_by("name")[:3]
    products = Product.objects.filter(is_active=True).order_by("-id")[:4]
    banner = Banner.objects.filter(id=1, is_active=True)

    if request.method == "POST":
        email = request.POST.get("subemail")
        
        SubEmail.objects.create(
            email=email,
        )

        return redirect(url)
    
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

    context = {
        'catogories': catogories,
        'products': products,
        'banner': banner,
    }

    return render(request, 'index.html', context)

def product(request):
    url = request.META.get('HTTP_REFERER')

    products = Product.objects.filter(is_active=True).order_by("-id")[:6]

    if request.method == "POST":
        email = request.POST.get("subemail")
        
        SubEmail.objects.create(
            email=email,
        )

        return redirect(url)

    context = {
        'products': products,
    }

    return render(request, 'product.html', context)

def detail(request, slug):
    url = request.META.get('HTTP_REFERER')

    product = Product.objects.filter(slug__iexact=slug, is_active=True).first()
    reviews = Review.objects.filter(product=product, is_active=True).order_by("-id")

    if request.method == "POST":
        email = request.POST.get("subemail")
        
        SubEmail.objects.create(
            email=email,
        )

        return redirect(url)

    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'detail.html', context)
