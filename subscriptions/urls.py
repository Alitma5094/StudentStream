from django.urls import path
from .views import subscriptions, sub_card, SubscriptionListView, SubscriptionDetailView

urlpatterns = [
    path("", SubscriptionListView.as_view(), name="subscription_list"),
    path("create/", subscriptions, name="subscription_create"),
    path("create/card/", sub_card, name="sub_card"),
    path("<str:pk>/", SubscriptionDetailView.as_view(), name="subscription_detail"),
]
