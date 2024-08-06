from django.urls import path

from apps.product.views import home, product, detail


urlpatterns = [
    path('', home, name="home"),
    path('product/', product, name="product"),
    path('detail/<slug:slug>/', detail, name="detail"),
]
