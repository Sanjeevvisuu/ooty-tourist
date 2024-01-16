"""
URL configuration for tourist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from website_app.urls import urlpatterns as website_app_urls
from product.urls import urlpatterns as product_urls
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
from contact.urls import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("website_app.urls")),
    path("product",include("product.urls")),
    path("booking",include("booking.urls")),
    path("contact",include("contact.urls")),
=======

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(website_app_urls, namespace='website')),
    path("product", include(product_urls, namespace='product')),
    path("booking", include("booking.urls", namespace='booking')),
>>>>>>> 11b0c7f8485b1db1e70008dd36ceaba44319e3bb
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
