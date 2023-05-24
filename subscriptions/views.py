import uuid
from django.conf import settings
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def subscriptions(request):
    if request.POST:
        phases = []
        for key in request.POST.keys():
            if "cadence" in key:
                tempdict = {}
                index = key.split("_")[1]
                tempdict["cadence"] = request.POST[f"cadence_{index}"]
                period = request.POST[f"period_{index}"]
                if period != "forever":
                    tempdict["periods"] = int(period)
                tempdict["recurring_price_money"] = {
                    "amount": int(request.POST[f"amount_{index}"]),
                    "currency": "USD",
                }
                tempdict["ordinal"] = int(index)

                phases.append(tempdict)

        result = settings.SQUARE_CLIENT.catalog.upsert_catalog_object(
            body={
                "idempotency_key": str(uuid.uuid4()),
                "object": {
                    "type": "SUBSCRIPTION_PLAN",
                    "id": "#plan",
                    "subscription_plan_data": {
                        "name": request.POST["name"],
                        "phases": phases,
                    },
                },
            }
        )

        if result.is_success():
            print(result.body)
        elif result.is_error():
            print(result.errors)
        return redirect("student_list")

    return render(request, "subscriptions/sub.html")


@login_required
def sub_card(request):
    if not request.GET["num"].isnumeric():
        return HttpResponseBadRequest("num must be an int")
    return render(
        request, "partials/sub_card.html", context={"num": request.GET["num"]}
    )


class SubscriptionListView(LoginRequiredMixin, TemplateView):
    template_name = "subscriptions/subscription_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        result = settings.SQUARE_CLIENT.catalog.list_catalog(types="SUBSCRIPTION_PLAN")

        if result.is_success():
            context["subscriptions"] = result.body["objects"]
        elif result.is_error():
            print(result.errors)
            self.template_name = "errors/error.html"

        return context


def get_sub(pk):
    result = settings.SQUARE_CLIENT.catalog.retrieve_catalog_object(object_id=pk)

    if result.is_success():
        return {"success": True, "data": result.body["object"]}
    else:
        print(result.errors)
        return {"success": False}


class SubscriptionDetailView(LoginRequiredMixin, TemplateView):
    template_name = "subscriptions/subscription_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        result = get_sub(self.kwargs["pk"])

        if result["success"]:
            context["subscription"] = result["data"]
        else:
            self.template_name = "errors/error.html"

        return context
