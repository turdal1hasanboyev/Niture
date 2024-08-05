from django.urls import path

from apps.user.views import about


urlpatterns = [
    path('about/', about, name='about'),
]
