from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed, assertContains


def test_view(client, django_user_model, monkeypatch):
    def mock_get_sub(pk):
        return {"success": True, "data": {"id": "123456"}}

    monkeypatch.setattr("subscriptions.views.get_sub", mock_get_sub)

    user = django_user_model.objects.create_user(username="root", password="Oscar5182")
    client.force_login(user)
    url = reverse("subscription_detail", kwargs={"pk": "123456"})
    response = client.get(url)
    assertTemplateUsed(response, "subscriptions/subscription_details.html")
    assertContains(response, "123456")
