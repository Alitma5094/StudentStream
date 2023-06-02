from django.urls import path
from .views import AccountDetailView, AccountUpdateView

urlpatterns = [
    path("", AccountDetailView.as_view(), name="account_detail"),
    path("update/", AccountUpdateView.as_view(), name="account_update"),
]
