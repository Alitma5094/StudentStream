from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from .models import CheckInEvent
from students.models import Student


class CheckInView(TemplateView):
    template_name = "attendance/check_in.html"


def search_results(request):
    query = request.POST.get("search")
    students = Student.objects.filter(
        Q(first_name__icontains=query) | Q(last_name__icontains=query)
    )
    context = {"students": students}
    return render(request, "partials/attendance_search_results.html", context)


def finish(request, pk):
    student = Student.objects.get(id=pk)
    CheckInEvent.objects.create(student=student)
    return render(request, "partials/attendance_success.html")
