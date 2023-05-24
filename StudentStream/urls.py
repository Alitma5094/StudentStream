from django.conf import settings  
from django.conf.urls.static import static  
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("subscriptions/", include("subscriptions.urls")),
    path("", include("pages.urls")),
]