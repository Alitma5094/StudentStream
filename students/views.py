from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student
from django.urls import reverse_lazy
from django.shortcuts import render
import uuid
from django.conf import settings
from ranks.models import RankPromotion, Rank


class StudentListView(ListView):
    model = Student
    context_object_name = "student_list"
    template_name = "students/student_list.html"


class StudentDetailView(DetailView):
    model = Student
    context_object_name = "student"
    template_name = "students/student_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ranks"] = Rank.objects.all()
        context["student_ranks"] = RankPromotion.objects.filter(student=context["student"])
        if context["student"].payment_id:
            result = settings.SQUARE_CLIENT.subscriptions.search_subscriptions(
                body={
                    "query": {
                        "filter": {"customer_ids": [context["student"].payment_id]}
                    }
                }
            ).body

            if result:
                context["subscriptions"] = result["subscriptions"]
            else:
                context["subscriptions"] = []
        else:
            context["subscriptions"] = []

        return context


class StudentCreateView(CreateView):
    model = Student
    template_name = "students/student_create.html"
    fields = "__all__"


class StudentUpdateView(UpdateView):
    model = Student
    template_name = "students/student_update.html"
    fields = "__all__"


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "students/student_delete.html"
    success_url = reverse_lazy("student_list")


def student_square_modal(request, pk):
    # TODO: Check if payment provider is already connected
    match request.GET.get("step"):
        case "ask":
            context = {"reference_id": uuid.uuid4(), "student_id": pk}
            print(context["reference_id"])
            return render(request, "partials/payment_connect_ask.html", context)
        case "merge":
            ref_id = request.GET.get("ref_id")
            result = settings.SQUARE_CLIENT.customers.search_customers(
                body={"query": {"filter": {"reference_id": {"exact": str(ref_id)}}}}
            )
            print(result)

            if result.is_error() or result.body == {}:
                print(result)
                return render(
                    request,
                    "partials/payment_connect_error.html",
                    context={"message": "finding the selected student"},
                )
            else:
                print("no error")
                square_id = result.body["customers"][0]["id"]
                print(square_id)
                student = Student.objects.get(id=pk)
                student.payment_id = square_id
                student.save()
                print("Saved")
            return render(request, "partials/payment_connect_success.html")
        case "new":
            student = Student.objects.get(id=pk)
            result = settings.SQUARE_CLIENT.customers.create_customer(
                body={
                    "idempotency_key": str(uuid.uuid4()),
                    "given_name": student.first_name,
                    "family_name": student.last_name,
                    # TODO Change email to selected primary email
                    "email_address": student.email,
                    # "address": {
                    #     "address_line_1": student.address,
                    #     "address_line_2": student.address2,
                    #     "postal_code": student.postal_code,
                    # },
                    "birthday": student.birthday.strftime("%Y-%m-%d"),
                }
            )

            if result.is_success():
                print(result.body)
                student.payment_id = result.body["customer"]["id"]
                student.save()
                return render(request, "partials/payment_connect_success.html")
            else:
                print(result.errors)
                return render(
                    request,
                    "partials/payment_connect_error.html",
                    context={"message": "creating a Square customer"},
                )
        case _:
            return render(request, "partials/payment_connect_error.html")


def create_rank(request, pk):
    student = Student.objects.get(id=pk)
    rank = Rank.objects.get(id=request.POST.get("rank"))
    RankPromotion.objects.create(
        date=request.POST.get("date"),
        belt_size=request.POST.get("belt_size"),
        rank=rank,
        student=student,
    )
    student.current_rank = rank
    student.save()
    ranks = Rank.objects.all()
    student_ranks = RankPromotion.objects.filter(student=student)
    context = {"ranks": ranks, "student_ranks": student_ranks}
    return render(request, "partials/students_ranks.html", context)


def delete_rank(request, pk):
    student_rank = RankPromotion.objects.get(id=pk)
    student_rank.delete()
    return HttpResponse("")
