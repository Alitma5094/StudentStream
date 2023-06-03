from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student
from django.urls import reverse_lazy


class StudentListView(ListView):
    model = Student
    context_object_name = "student_list"
    template_name = "students/student_list.html"


class StudentDetailView(DetailView):
    model = Student
    context_object_name = "student"
    template_name = "students/student_detail.html"


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
