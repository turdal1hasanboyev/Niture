from django.urls import path

from apps.blog.views import blog


urlpatterns = [
    path('blog/', blog, name='blog'),
]
