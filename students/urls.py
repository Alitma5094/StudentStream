from django.urls import path
from .views import (
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
    student_square_modal,
    create_rank,
    delete_rank
)

urlpatterns = [
    path("", StudentListView.as_view(), name="student_list"),
    path("<uuid:pk>/", StudentDetailView.as_view(), name="student_detail"),
    path("create/", StudentCreateView.as_view(), name="student_create"),
    path("<uuid:pk>/update/", StudentUpdateView.as_view(), name="student_update"),
    path("<uuid:pk>/delete/", StudentDeleteView.as_view(), name="student_delete"),
    path("<uuid:pk>/modal/", student_square_modal, name="student_square_modal"),
    path("<uuid:pk>/update_rank/", create_rank, name="create_rank"),
    path("<uuid:pk>/delete_rank/", delete_rank, name="delete_rank"),
]
