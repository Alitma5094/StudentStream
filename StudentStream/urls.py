from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("accounts.urls")),
    path("attendance/", include("attendance.urls")),
    path("subscriptions/", include("subscriptions.urls")),
    path("students/", include("students.urls")),
    path("ranks/", include("ranks.urls")),
    path('sentry-debug/', trigger_error),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", include("pages.urls")),
]
