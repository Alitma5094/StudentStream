from django.urls import path

from .views import search_results, CheckInView, finish

urlpatterns = [
    path("search/", search_results, name="search_results"),
    path("save/<uuid:pk>/", finish, name="check_in_save"),
    path("", CheckInView.as_view(), name="check_in"),
]
